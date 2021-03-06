"""Contsructor to take a Python dict containing an API Documentation and
create a HydraDoc object for it
"""
import re
import json
from hydra_python_core.doc_writer import (HydraDoc, HydraClass, HydraClassProp,
                                          HydraClassOp, HydraStatus, HydraLink)
from typing import Any, Dict, Match, Optional, Tuple, Union


def error_mapping(body: str=None) -> str:
    """Function returns starting error message based on its body type.
    :param body: Params type for error message
    :return string: Error message for input key
    """
    error_map = {
        "doc": "The API Documentation must have",
        "class_dict": "Class must have",
        "supported_prop": "Property must have",
        "link_prop": "Link property must have",
        "supported_op": "Operation must have",
        "possible_status": "Status must have"
    }
    return error_map[body]


def input_key_check(
        body: Dict[str, Any], key: str = None,
        body_type: str = None, literal: bool = False) -> dict:
    """Function to validate key inside the dictonary payload
    :param body: JSON body in which we have to check the key
    :param key: To check if its value exit in the body
    :param body_type: Name of JSON body
    :param literal: To check whether we need to convert the value
    :return string: Value of the body

    Raises:
        SyntaxError: If the `body` does not include any entry for `key`.

    """
    try:
        if literal:
            return convert_literal(body[key])
        return body[key]
    except KeyError:
        raise SyntaxError("{0} [{1}]".format(error_mapping(body_type), key))


def create_doc(doc: Dict[str, Any], HYDRUS_SERVER_URL: str = None,
               API_NAME: str = None) -> HydraDoc:
    """Create the HydraDoc object from the API Documentation.

    Raises:
        SyntaxError: If the `doc` doesn't have an entry for `@id` key.
        SyntaxError: If the `@id` key of the `doc` is not of
            the form : '[protocol] :// [base url] / [entrypoint] / vocab'

    """
    # Check @id
    try:
        id_ = doc["@id"]
    except KeyError:
        raise SyntaxError("The API Documentation must have [@id]")

    # Extract base_url, entrypoint and API name
    match_obj = re.match(r'(.*)://(.*)/(.*)/vocab#?', id_, re.M | re.I)
    if match_obj:
        base_url = "{0}://{1}/".format(match_obj.group(1), match_obj.group(2))
        entrypoint = match_obj.group(3)

    # Syntax checks
    else:
        raise SyntaxError(
            "The '@id' of the Documentation must be of the form:\n"
            "'[protocol] :// [base url] / [entrypoint] / vocab'")
    doc_keys = {
        "description": False,
        "title": False,
        "supportedClass": False,
        "@context": False,
        "possibleStatus": False
    }
    result = {}
    for k, literal in doc_keys.items():
        result[k] = input_key_check(doc, k, "doc", literal)

    # EntryPoint object
    # getEntrypoint checks if all classes have @id
    entrypoint_obj = get_entrypoint(doc)

    # Main doc object
    if HYDRUS_SERVER_URL is not None and API_NAME is not None:
        apidoc = HydraDoc(
            API_NAME, result["title"], result["description"], API_NAME, HYDRUS_SERVER_URL)
    else:
        apidoc = HydraDoc(
            entrypoint, result["title"], result["description"], entrypoint, base_url)

    # additional context entries
    for entry in result["@context"]:
        apidoc.add_to_context(entry, result["@context"][entry])

    # add all parsed_classes
    for class_ in result["supportedClass"]:
        class_obj, collection, collection_path = create_class(
            entrypoint_obj, class_)
        if class_obj:
            if "manages" in class_:
                apidoc.add_supported_class(
                    class_obj, collection=collection, collection_path=collection_path,
                    collection_manages=class_["manages"])
            else:
                apidoc.add_supported_class(
                    class_obj, collection=collection, collection_path=collection_path)

    # add possibleStatus
    for status in result["possibleStatus"]:
        status_obj = create_status(status)
        apidoc.add_possible_status(status_obj)

    apidoc.add_baseResource()
    apidoc.add_baseCollection()
    apidoc.gen_EntryPoint()
    return apidoc


def create_class(
        entrypoint: Dict[str, Any],
        class_dict: Dict[str, Any]) -> Tuple[HydraClass, bool, str]:
    """Create HydraClass objects for classes in the API Documentation."""
    # Base classes not used
    exclude_list = ['http://www.w3.org/ns/hydra/core#Resource',
                    'http://www.w3.org/ns/hydra/core#Collection',
                    entrypoint["@id"]]
    id_ = class_dict["@id"]
    if id_ in exclude_list:
        return None, None, None
    match_obj = re.match(r'vocab:(.*)', id_, re.M | re.I)
    if match_obj:
        id_ = match_obj.group(1)

    doc_keys = {
        "supportedProperty": False,
        "title": False,
        "description": False,
        "supportedOperation": False
    }

    result = {}
    for k, literal in doc_keys.items():
        result[k] = input_key_check(class_dict, k, "class_dict", literal)

    # See if class_dict is a Collection Class
    # type: Union[Match[Any], bool]
    collection = re.match(r'(.*)Collection(.*)', result["title"], re.M | re.I)
    if collection:
        return None, None, None

    # Check if class has it's own endpoint
    endpoint, path = class_in_endpoint(class_dict, entrypoint)

    # Check if class has a Collection
    collection, collection_path = collection_in_endpoint(
        class_dict, entrypoint)

    # Create the HydraClass object
    class_ = HydraClass(
        id_, result["title"], result["description"], path, endpoint=endpoint)

    # Add supportedProperty for the Class
    for prop in result["supportedProperty"]:
        prop_obj = create_property(prop)
        class_.add_supported_prop(prop_obj)

    # Add supportedOperation for the Class
    for op in result["supportedOperation"]:
        op_obj = create_operation(op)
        class_.add_supported_op(op_obj)

    return class_, collection, collection_path


def get_entrypoint(doc: Dict[str, Any]) -> Dict[str, Any]:
    """Find and return the entrypoint object in the doc.

    Raises:
        SyntaxError: If any supportedClass in the API Documentation does
            not have an `@id` key.
        SyntaxError: If no EntryPoint is found when searching in the Api Documentation.

    """

    # Search supportedClass
    for class_ in doc["supportedClass"]:
        # Check the @id for each class
        try:
            class_id = class_["@id"]
        except KeyError:
            raise SyntaxError("Each supportedClass must have [@id]")
        # Match with regular expression
        match_obj = re.match(r'vocab:(.*)EntryPoint', class_id)
        # Return the entrypoint object
        if match_obj:
            return class_
    # If not found, raise error
    raise SyntaxError("No EntryPoint class found")


def convert_literal(literal: Any) -> Optional[Union[bool, str]]:
    """Convert JSON literals to Python ones.

    Raises:
        TypeError: If `literal` is not a boolean value, a string or None.

    """

    # Map for the literals
    map_ = {
        "true": True,
        "false": False,
        "null": None
    }
    # Check if literal is in string format
    if isinstance(literal, str):
        # Check if the literal is valid
        if literal in map_:
            return map_[literal]
        return literal
    elif isinstance(literal, (bool,)) or literal is None:
        return literal
    else:
        # Raise error for non string objects
        raise TypeError("Literal not recognised")


def create_property(supported_prop: Dict[str, Any]) -> HydraClassProp:
    """Create a HydraClassProp object from the supportedProperty."""
    # Syntax checks

    doc_keys = {
        "property": False,
        "title": False,
        "readable": True,
        "writeable": True,
        "required": True
    }
    result = {}
    for k, literal in doc_keys.items():
        result[k] = input_key_check(
            supported_prop, k, "supported_prop", literal)
    # Check if it's a link property
    if isinstance(result["property"], Dict):
        result["property"] = create_link_property(result["property"])
    # Create the HydraClassProp object
    prop = HydraClassProp(result["property"], result["title"], required=result["required"],
                          read=result["readable"], write=result["writeable"])
    return prop


def create_link_property(
        link_prop_dict: Dict[str, Any]) -> HydraLink:
    """Create HydraLink objects for link properties in the API Documentation."""
    id_ = link_prop_dict["@id"]

    doc_keys = {
        "title": False,
        "description": False,
        "supportedOperation": False,
        "range": False,
        "domain": False
    }

    result = {}
    for k, literal in doc_keys.items():
        result[k] = input_key_check(link_prop_dict, k, "link_prop", literal)

    # Create the HydraLink object
    link = HydraLink(
        id_, result["title"], result["description"], result["domain"], result["range"])

    # Add supportedOperation for the Link
    for op in result["supportedOperation"]:
        op_obj = create_operation(op)
        link.add_supported_op(op_obj)

    return link


def class_in_endpoint(
        class_: Dict[str, Any], entrypoint: Dict[str, Any]) -> Tuple[bool, bool]:
    """Check if a given class is in the EntryPoint object as a class.

    Raises:
        SyntaxError: If the `entrypoint` dictionary does not include the key
            `supportedProperty`.
        SyntaxError: If any dictionary in `supportedProperty` list does not include
            the key `property`.
        SyntaxError: If any property dictionary does not include the key `label`.

    """
    # Check supportedProperty for the EntryPoint
    try:
        supported_property = entrypoint["supportedProperty"]
    except KeyError:
        raise SyntaxError("EntryPoint must have [supportedProperty]")

    # Check all endpoints in supportedProperty
    for prop in supported_property:
        # Syntax checks
        try:
            property_ = prop["property"]
        except KeyError:
            raise SyntaxError("supportedProperty must have [property]")
        try:
            label = property_["label"]
        except KeyError:
            raise SyntaxError("property must have [label]")
        # Match the title with regular expression

        if label == class_['title']:
            path = "/".join(property_['@id'].split("/")[1:])
            return True, path
    return False, None


def collection_in_endpoint(
        class_: Dict[str, Any], entrypoint: Dict[str, Any]) -> Tuple[bool, bool]:
    """Check if a given class is in the EntryPoint object as a collection.

    Raises:
        SyntaxError: If the `entrypoint` dictionary does not include the key
            `supportedProperty`.
        SyntaxError: If any dictionary in `supportedProperty` list does not include
            the key `property`.
        SyntaxError: If any property dictionary does not include the key `label`.

    """
    # Check supportedProperty for the EntryPoint
    try:
        supported_property = entrypoint["supportedProperty"]
    except KeyError:
        raise SyntaxError("EntryPoint must have [supportedProperty]")

    # Check all endpoints in supportedProperty
    for prop in supported_property:
        # Syntax checks
        try:
            property_ = prop["property"]
        except KeyError:
            raise SyntaxError("supportedProperty must have [property]")
        try:
            label = property_["label"]
        except KeyError:
            raise SyntaxError("property must have [label]")
        # Match the title with regular expression
        if label == "{}Collection".format(class_["title"]):
            path = "/".join(property_['@id'].split("/")[1:])
            return True, path
    return False, None


def create_operation(supported_op: Dict[str, Any]) -> HydraClassOp:
    """Create a HyraClassOp object from the supportedOperation."""
    # Syntax checks
    doc_keys = {
        "title": False,
        "method": False,
        "expects": True,
        "returns": True,
        "expectsHeader": False,
        "returnsHeader": False,
        "possibleStatus": False
    }
    result = {}
    for k, literal in doc_keys.items():
        result[k] = input_key_check(supported_op, k, "supported_op", literal)
    possible_statuses = list()
    for status in result["possibleStatus"]:
        status_obj = create_status(status)
        possible_statuses.append(status_obj)

    # Create the HydraClassOp object
    op_ = HydraClassOp(result["title"], result["method"],
                       result["expects"], result["returns"],
                       result["expectsHeader"], result["returnsHeader"],
                       possible_statuses)
    return op_


def create_status(possible_status: Dict[str, Any]) -> HydraStatus:
    """Create a HydraStatus object from the possibleStatus."""
    # Syntax checks
    doc_keys = {
        "title": False,
        "statusCode": False,
        "description": True
    }
    result = {}
    for k, literal in doc_keys.items():
        result[k] = input_key_check(
            possible_status, k, "possible_status", literal)
    # Create the HydraStatus object
    status = HydraStatus(result["statusCode"],
                         result["title"], result["description"])
    return status
