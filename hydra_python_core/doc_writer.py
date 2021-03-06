"""API Doc templates generator."""
from typing import Any, Dict, List, Optional, Union


class HydraDoc():
    """Class for an API Doc."""

    def __init__(self, API: str, title: str, desc: str,
                 entrypoint: str, base_url: str) -> None:
        """Initialize the APIDoc."""
        self.API = API
        self.title = title
        self.base_url = base_url
        self.context = Context("{}{}".format(base_url, API))
        self.parsed_classes = dict()  # type: Dict[str, Any]
        self.other_classes = list()  # type: List[HydraClass]
        self.collections = dict()  # type: Dict[str, Any]
        # type: List[Union[HydraStatus,HydraError]]
        self.possible_status = list()
        self.entrypoint = HydraEntryPoint(base_url, entrypoint)
        self.desc = desc

    def add_supported_class(
            self, class_: 'HydraClass', collection: Union[bool, 'HydraCollection']=False,
            collection_path: str=None, collectionGet: bool=True, collectionPost: bool=True,
            collection_manages: Union[Dict[str, Any], List]=None) -> None:
        """Add a new supportedClass.

        Raises:
            TypeError: If `class_` is not an instance of `HydraClass`

        """
        # self.doc["supportedClass"].append(class_.get())
        if not isinstance(class_, HydraClass):
            raise TypeError("Type is not <HydraClass>")
        self.parsed_classes[class_.path] = {
            "context": Context(address="{}{}".format(self.base_url, self.API), class_=class_),
            "class": class_,
            "collection": collection
        }
        if collection:
            collection = HydraCollection(
                class_, collection_path, collection_manages, collectionGet, collectionPost)
            self.collections[collection.path] = {
                "context": Context(address="{}{}".format(self.base_url, self.API),
                                   collection=collection), "collection": collection}

    def add_possible_status(self, status: Union['HydraStatus', 'HydraError']) -> None:
        """Add a new possibleStatus.

        Raises:
            TypeError: If `status` is not an instance of `HydraStatus`.

        """
        if not isinstance(status, HydraStatus):
            raise TypeError("Type is not <HydraStatus>")
        self.possible_status.append(status)

    def add_baseCollection(self) -> None:
        """Add Collection class to the API Doc."""
        collection = HydraClass(
            "http://www.w3.org/ns/hydra/core#Collection", "Collection", None)
        member = HydraClassProp(
            "http://www.w3.org/ns/hydra/core#member", "members", False, False, None)
        collection.add_supported_prop(member)
        self.other_classes.append(collection)

    def add_baseResource(self) -> None:
        """Add Resource class to the API Doc."""
        resource = HydraClass(
            "http://www.w3.org/ns/hydra/core#Resource", "Resource", None)
        self.other_classes.append(resource)

    def add_to_context(
            self, key: str, value: Union[Dict[str, str], str]) -> None:
        """Add entries to the vocabs context."""
        self.context.add(key, value)

    def gen_EntryPoint(self) -> None:
        """Generate the EntryPoint for the Hydra Doc."""
        # pdb.set_trace()
        for class_ in self.parsed_classes:
            if self.parsed_classes[class_]["class"].endpoint:
                self.entrypoint.add_Class(self.parsed_classes[class_]["class"])
        for collection in self.collections:
            self.entrypoint.add_Collection(
                self.collections[collection]["collection"])

    def generate(self) -> Dict[str, Any]:
        """Get the Hydra API Doc as a python dict."""
        parsed_classes = [self.parsed_classes[key]["class"]
                          for key in self.parsed_classes]
        collections = [self.collections[key]["collection"]
                       for key in self.collections]
        doc = {
            "@context": self.context.generate(),
            "@id": "{}{}/vocab".format(self.base_url, self.API),
            "@type": "ApiDocumentation",
            "title": self.title,
            "description": self.desc,
            "supportedClass": [
                x.generate() for x in parsed_classes +
                self.other_classes + collections + [self.entrypoint]],
            "possibleStatus": [status.generate() for status in self.possible_status]
        }
        return doc


class HydraClass():
    """Template for a new class."""

    def __init__(
            self, id_: str, title: str, desc: str, path: str=None,
            endpoint: bool=False, sub_classof: None=None) -> None:
        """Initialize the Hydra_Class."""
        self.id_ = id_ if "http" in id_ else "vocab:{}".format(id_)
        self.title = title
        self.desc = desc
        self.path = path if path else title
        self.parents = None
        self.endpoint = endpoint
        self.supportedProperty = list()  # type: List
        self.supportedOperation = list()  # type: List
        if sub_classof is not None:
            self.parents = sub_classof

    def add_supported_prop(
            self, prop: Union['HydraClassProp', 'EntryPointClass', 'EntryPointCollection']) -> None:
        """Add a new supportedProperty.

        Raises:
            TypeError: If `prop` is not an instance of `HydraClassProp` or `EntryPointClass`
                or `EntryPointCollection`

        """
        if not isinstance(
                prop, (HydraClassProp, EntryPointClass, EntryPointCollection)):
            raise TypeError("Type is not <HydraClassProp>")
        self.supportedProperty.append(prop)

    def add_supported_op(
            self, op: Union['EntryPointOp', 'HydraClassOp']) -> None:
        """Add a new supportedOperation.

        Raises:
            TypeError: If `op` is not an instance of `HydraClassOp` or `EntryPointOp`

        """
        if not isinstance(op, (HydraClassOp, EntryPointOp)):
            raise TypeError("Type is not <HydraClassOp>")
        self.supportedOperation.append(op)

    def generate(self) -> Dict[str, Any]:
        """Get the Hydra class as a python dict."""
        class_ = {
            "@id": self.id_,
            "@type": "hydra:Class",
            "title": self.title,
            "description": self.desc,
            "supportedProperty": [x.generate() for x in self.supportedProperty],
            "supportedOperation": [x.generate() for x in self.supportedOperation],
        }
        if self.parents is not None:
            class_["subClassOf"] = self.parents
        return class_


class HydraClassProp():
    """Template for a new property."""

    def __init__(self,
                 prop: Union[str, 'HydraLink'],
                 title: str,
                 read: bool,
                 write: bool,
                 required: bool,
                 desc: str = "",
                 ) -> None:
        """Initialize the Hydra_Prop."""
        self.prop = prop
        self.title = title
        self.read = read
        self.write = write
        self.required = required
        self.desc = desc

    def generate(self) -> Dict[str, Any]:
        """Get the Hydra prop as a python dict."""
        prop = {
            "@type": "SupportedProperty",
            "title": self.title,
            "required": self.required,
            "readable": self.read,
            "writeable": self.write
        }
        if isinstance(self.prop, HydraLink):
            prop["property"] = self.prop.generate()
        else:
            prop["property"] = self.prop
        if len(self.desc) > 0:
            prop["description"] = self.desc
        return prop


class HydraClassOp():
    """Template for a new supportedOperation."""

    def __init__(self,
                 title: str,
                 method: str,
                 expects: Optional[str],
                 returns: Optional[str],
                 expects_header: List[str] = [],
                 returns_header: List[str] = [],
                 possible_status: List[Union['HydraStatus', 'HydraError']]=[],
                 ) -> None:
        """Initialize the Hydra_Prop."""
        self.title = title
        self.method = method
        self.expects = expects
        self.returns = returns
        self.expects_header = expects_header
        self.returns_header = returns_header
        self.possible_status = possible_status

    def get_type(self, method: str) -> str:
        """Return @type for op based on method type."""
        if method == "POST":
            return "http://schema.org/UpdateAction"
        elif method == "PUT":
            return "http://schema.org/AddAction"
        elif method == "DELETE":
            return "http://schema.org/DeleteAction"
        else:
            return "http://schema.org/FindAction"

    def generate(self) -> Dict[str, Any]:
        """Get the Hydra op as a python dict."""
        op = {
            "@type": self.get_type(self.method),
            "title": self.title,
            "method": self.method,
            "expects": self.expects,
            "returns": self.returns,
            "expectsHeader": self.expects_header,
            "returnsHeader": self.returns_header,
            "possibleStatus": [status.generate() for status in self.possible_status]
        }
        return op


class HydraCollection():
    """Class for Hydra Collection."""

    def __init__(
            self, class_: HydraClass,
            collection_path: str=None, manages: Union[Dict[str, Any], List]=None,
            get: bool=True, post: bool=True) -> None:
        """Generate Collection for a given class."""
        self.class_ = class_
        self.name = "{}Collection".format(class_.title)
        self.path = collection_path if collection_path else self.name
        self.manages = manages
        self.supportedOperation = list()  # type: List
        self.supportedProperty = [HydraClassProp("http://www.w3.org/ns/hydra/core#member",
                                                 "members",
                                                 False, False, False,
                                                 "The {}".format(self.class_.title.lower()))]

        if get:
            get_op = HydraCollectionOp("_:{}_collection_retrieve".format(self.class_.title.lower()),
                                       "http://schema.org/FindAction",
                                       "GET", "Retrieves all {} entities".format(
                                           self.class_.title),
                                       None, "vocab:{}".format(self.name), [], [], [])
            self.supportedOperation.append(get_op)

        if post:
            post_op = HydraCollectionOp("_:{}_create".format(self.class_.title.lower()),
                                        "http://schema.org/AddAction",
                                        "PUT", "Create new {} entity".format(
                                            self.class_.title),
                                        self.class_.id_, self.class_.id_, [], [],
                                        [HydraStatus(code=201, desc="If the {} entity was created"
                                                     "successfully.".format(self.class_.title))]
                                        )
            self.supportedOperation.append(post_op)

    def generate(self) -> Dict[str, Any]:
        """Get as a python dict."""
        collection = {
            "@id": "vocab:{}".format(self.name,),
            "@type": "hydra:Class",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "title": "{}".format(self.name),
            "description": "A collection of {}".format(self.class_.title.lower()),
            "supportedOperation": [x.generate() for x in self.supportedOperation],
            "supportedProperty": [x.generate() for x in self.supportedProperty]
        }
        if self.manages is not None:
            collection["manages"] = self.manages
        return collection


class HydraCollectionOp():
    """Operation class for Collection operations."""

    def __init__(self,
                 id_: str,
                 type_: str,
                 method: str,
                 desc: str,
                 expects: Optional[str],
                 returns: Optional[str],
                 expects_header: List[str] = [],
                 returns_header: List[str] = [],
                 possible_status: List[Union['HydraStatus', 'HydraError']]=[],
                 ) -> None:
        """Create method."""
        self.id_ = id_
        self.type_ = type_
        self.method = method
        self.desc = desc
        self.expects = expects
        self.returns = returns
        self.expects_header = expects_header
        self.returns_header = returns_header
        self.possible_status = possible_status

    def generate(self) -> Dict[str, Any]:
        """Get as a Python dict."""
        object_ = {
            "@id": self.id_,
            "@type": self.type_,
            "method": self.method,
            "description": self.desc,
            "expects": self.expects,
            "returns": self.returns,
            "expectsHeader": self.expects_header,
            "returnsHeader": self.returns_header,
            "possibleStatus": [status.generate() for status in self.possible_status]
        }
        return object_


class HydraEntryPoint():
    """Template for a new entrypoint."""

    def __init__(self, base_url: str, entrypoint: str) -> None:
        """Initialize the Entrypoint."""
        self.url = base_url
        self.api = entrypoint
        self.entrypoint = HydraClass(
            "EntryPoint", "EntryPoint", "The main entry point or homepage of the API.")
        self.entrypoint.add_supported_op(EntryPointOp(
            "_:entry_point", "GET", "The APIs main entry point.", None, None,
            type_="vocab:EntryPoint"))
        self.context = Context(
            "{}{}".format(
                base_url,
                entrypoint),
            entrypoint=self)

    def add_Class(self, class_: HydraClass) -> None:
        """Add supportedProperty to the EntryPoint.

        Raises:
            TypeError: If `class_` is not an instance of `HydraClass`.

        """
        if not isinstance(class_, HydraClass):
            raise TypeError("Type is not <HydraClass>")
        entrypoint_class = EntryPointClass(class_)
        self.entrypoint.add_supported_prop(entrypoint_class)
        self.context.add(entrypoint_class.name, {
                         "@id": entrypoint_class.id_, "@type": "@id"})

    def add_Collection(self, collection: HydraCollection) -> None:
        """Add supportedProperty to the EntryPoint.

        Raises:
            TypeError: If `collection` is not an instance of `HydraCollection`.

        """
        if not isinstance(collection, HydraCollection):
            raise TypeError("Type is not <HydraCollection>")
        entrypoint_collection = EntryPointCollection(collection)
        self.entrypoint.add_supported_prop(entrypoint_collection)
        self.context.add(entrypoint_collection.name, {
                         "@id": entrypoint_collection.id_, "@type": "@id"})

    def generate(self) -> Dict[str, Any]:
        """Get as a Python dict."""
        return self.entrypoint.generate()

    def get(self) -> Dict[str, str]:
        """Create the EntryPoint object to be returnd for the get function."""
        object_ = {
            "@context": "/{}/contexts/EntryPoint.jsonld".format(self.api),
            "@id": "/{}".format(self.api),
            "@type": "EntryPoint",
        }
        for item in self.entrypoint.supportedProperty:
            uri = item.id_
            object_[item.name] = uri.replace(
                "vocab:EntryPoint", "/{}".format(self.api))

        return object_


class EntryPointCollection():
    """Class for a Collection Entry to the EntryPoint object."""

    def __init__(self, collection: HydraCollection) -> None:
        """Create method."""
        self.name = collection.name
        self.supportedOperation = collection.supportedOperation
        if collection.path:
            self.id_ = "vocab:EntryPoint/{}".format(collection.path)
        else:
            self.id_ = "vocab:EntryPoint/{}".format(self.name)

    def generate(self) -> Dict[str, Any]:
        """Get as a python dict."""
        object_ = {
            "property": {
                "@id": self.id_,
                "@type": "hydra:Link",
                "label": self.name,
                "description": "The {} collection".format(self.name,),
                "domain": "vocab:EntryPoint",
                "range": "vocab:{}".format(self.name,),
                "supportedOperation": []
            },
            "hydra:title": self.name.lower(),
            "hydra:description": "The {} collection".format(self.name,),
            "required": None,
            "readable": True,
            "writeable": False
        }  # type: Dict[str, Any]
        for op in self.supportedOperation:
            operation = EntryPointOp(op.id_.lower(), op.method,
                                     op.desc, op.expects, op.returns,
                                     op.expects_header, op.returns_header,
                                     op.possible_status,
                                     type_=op.type_)
            object_["property"]["supportedOperation"].append(
                operation.generate())
        return object_


class EntryPointClass():
    """Class for a Operation Entry to the EntryPoint object."""

    def __init__(self, class_: HydraClass) -> None:
        """Create method."""
        self.name = class_.title
        self.desc = class_.desc
        self.supportedOperation = class_.supportedOperation
        if class_.path:
            self.id_ = "vocab:EntryPoint/{}".format(class_.path)
        else:
            self.id_ = "vocab:EntryPoint/{}".format(self.name)

    def generate(self) -> Dict[str, Any]:
        """Get as Python Dict."""
        object_ = {
            "property": {
                "@id": self.id_,
                "@type": "hydra:Link",
                "label": self.name,
                "description": self.desc,
                "domain": "vocab:EntryPoint",
                "range": "vocab:{}".format(self.name),
                "supportedOperation": []
            },
            "hydra:title": self.name.lower(),
            "hydra:description": "The {} Class".format(self.name),
            "required": None,
            "readable": True,
            "writeable": False
        }  # type: Dict[str, Any]
        for op in self.supportedOperation:
            operation = EntryPointOp(op.title.lower(), op.method,
                                     None, op.expects, op.returns, op.expects_header,
                                     op.returns_header, op.possible_status,
                                     label=op.title)
            object_["property"]["supportedOperation"].append(
                operation.generate())
        return object_


class EntryPointOp():
    """supportedOperation for EntryPoint."""

    def __init__(self,
                 id_: str,
                 method: str,
                 desc: str,
                 expects: Optional[str],
                 returns: Optional[str],
                 expects_header: List[str] = [],
                 returns_header: List[str] = [],
                 possible_status: List[Union['HydraStatus', 'HydraError']]=[],
                 type_: Optional[str] = None,
                 label: str = "",
                 ) -> None:
        """Create method."""
        self.id_ = id_
        self.method = method
        self.desc = desc
        self.expects = expects
        self.returns = returns
        self.expects_header = expects_header
        self.returns_header = returns_header
        self.possible_status = possible_status
        self.label = label
        self.type_ = type_

    def get_type(self, method: str) -> str:
        """Return @type for op based on method type."""
        if method == "POST":
            return "http://schema.org/UpdateAction"
        elif method == "PUT":
            return "http://schema.org/AddAction"
        elif method == "DELETE":
            return "http://schema.org/DeleteAction"
        else:
            return "http://schema.org/FindAction"

    def generate(self) -> Dict[str, Any]:
        """Get as Python Dict."""
        prop = {
            "@id": self.id_,
            "@type": self.get_type(self.method),
            "method": self.method,
            "description": self.desc,
            "expects": self.expects,
            "returns": self.returns,
            "expectsHeader": self.expects_header,
            "returnsHeader": self.returns_header,
            "possibleStatus": [status.generate() for status in self.possible_status]
        }
        if self.type_ is not None:
            prop["@type"] = self.type_
        if len(self.label) > 0:
            prop["label"] = self.label
        return prop


class IriTemplateMapping():
    """Class for hydra IriTemplateMapping"""

    def __init__(self,
                 variable: str,
                 prop: str,
                 required: bool = False):
        self.variable = variable
        self.prop = prop
        self.required = required

    def generate(self) -> Dict[str, Any]:
        """Get IriTemplateMapping as a python dict"""
        iri_template_mapping = {
            "@type": "IriTemplateMapping",
            "variable": self.variable,
            "property": self.prop,
            "required": self.required
        }
        return iri_template_mapping


class HydraIriTemplate():
    """Class for hydra IriTemplates"""

    def __init__(self,
                 template: str,
                 iri_mapping: List[IriTemplateMapping] = [],
                 basic_representation: bool = True):
        self.template = template
        if basic_representation:
            self.variable_rep = "hydra:BasicRepresentation"
        else:
            self.variable_rep = "hydra:ExplicitRepresentation"
        self.mapping = iri_mapping

    def generate(self) -> Dict[str, Any]:
        """Get IriTemplate as a python dict"""
        iri_template = {
            "@type": "IriTemplate",
            "template": self.template,
            "variableRepresentation": self.variable_rep,
            "mapping": [x.generate() for x in self.mapping]
        }
        return iri_template


class HydraStatus():
    """Class for possibleStatus in Hydra Doc."""

    def __init__(self, code: int, id_: str = None, title: str = "", desc: str = "") -> None:
        """Create method."""
        self.code = code
        self.id_ = id_
        self.title = title
        self.desc = desc

    def generate(self, status_type: str = "Status") -> Dict[str, Any]:
        """Get as Python dict."""
        status = {
            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
            "@type": status_type,
            "statusCode": self.code,
            "title": self.title,
            "description": self.desc,
        }
        if self.id_ is not None:
            status["@id"] = self.id_
        return status


class HydraError(HydraStatus):
    """Class for Hydra Error to represent error details."""

    def __init__(self, code: int, id_: str = None, title: str = "", desc: str = "") -> None:
        """Create method"""
        super().__init__(code, id_, title, desc)

    def generate(self) -> Dict[str, Any]:
        """Get error response body"""
        error = HydraStatus.generate(self, status_type="Error")
        return error


class HydraLink():
    """Template for a link property."""

    def __init__(
            self, id_: str, title: str = "",
            desc: str = "", domain: str = "", range_: str = "") -> None:
        """Initialize the Hydra_Link."""
        self.id_ = id_ if "http" in id_ else "vocab:{}".format(id_)
        self.range = range_
        self.title = title
        self.desc = desc
        self.domain = domain
        self.supportedOperation = list()  # type: List

    def add_supported_op(
            self, op: Union['EntryPointOp', 'HydraClassOp']) -> None:
        """Add a new supportedOperation.

        Raises:
            TypeError: If `op` is not an instance of `HydraClassOp` or `EntryPointOp`

        """
        if not isinstance(op, (HydraClassOp, EntryPointOp)):
            raise TypeError("Type is not <HydraClassOp>")
        self.supportedOperation.append(op)

    def generate(self) -> Dict[str, Any]:
        """Get the Hydra link as a python dict."""
        link = {
            "@id": self.id_,
            "@type": "hydra:Link",
            "title": self.title,
            "description": self.desc,
            "range": self.range,
            "domain": self.domain,
            "supportedOperation": [x.generate() for x in self.supportedOperation],
        }
        return link


class Context():
    """Class for JSON-LD context."""

    def __init__(self,
                 address: str,
                 adders: Dict = {},
                 class_: Optional[HydraClass] = None,
                 collection: Optional[HydraCollection] = None,
                 entrypoint: Optional[HydraEntryPoint] = None,
                 ) -> None:
        """Initialize context."""
        # NOTE: adders is a dictionary containing additional
        # context elements to the base Hydra context
        if class_ is not None:
            self.context = {
                "vocab": "{}/vocab#".format(address),
                "hydra": "http://www.w3.org/ns/hydra/core#",
                "members": "http://www.w3.org/ns/hydra/core#member",
                "object": "http://schema.org/object",
            }  # type: Dict[str, Any]
            self.context[class_.title] = class_.id_
            for prop in class_.supportedProperty:
                self.context[prop.title] = prop.prop

        elif collection is not None:
            self.context = {
                "vocab": "{}/vocab#".format(address),
                "hydra": "http://www.w3.org/ns/hydra/core#",
                "members": "http://www.w3.org/ns/hydra/core#member",
            }
            self.context[collection.name] = "vocab:{}".format(collection.name)
            self.context[collection.class_.title] = collection.class_.id_

        elif entrypoint is not None:
            self.context = {
                "EntryPoint": "vocab:EntryPoint",
                "vocab": "{}/vocab#".format(address)
            }

        else:
            self.context = {
                "hydra": "http://www.w3.org/ns/hydra/core#",
                "property": {
                    "@type": "@id",
                    "@id": "hydra:property"
                },
                "supportedClass": "hydra:supportedClass",
                "supportedProperty": "hydra:supportedProperty",
                "supportedOperation": "hydra:supportedOperation",
                "label": "rdfs:label",
                "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
                "vocab": "{}/vocab#".format(address),
                # "vocab": "localhost/api/vocab#",
                "domain": {
                    "@type": "@id",
                    "@id": "rdfs:domain"
                },
                "ApiDocumentation": "hydra:ApiDocumentation",
                "range": {
                    "@type": "@id",
                    "@id": "rdfs:range"
                },
                "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
                "title": "hydra:title",
                "expects": {
                    "@type": "@id",
                    "@id": "hydra:expects"
                },
                "returns": {
                    "@id": "hydra:returns",
                    "@type": "@id"
                },
                "readable": "hydra:readable",
                "writeable": "hydra:writeable",
                "possibleStatus": "hydra:possibleStatus",
                "required": "hydra:required",
                "method": "hydra:method",
                "statusCode": "hydra:statusCode",
                "description": "hydra:description",
                "expectsHeader": "hydra:expectsHeader",
                "returnsHeader": "hydra:returnsHeader",
                "manages": "hydra:manages",
                "subClassOf": {
                    "@id": "rdfs:subClassOf",
                    "@type": "@id"
                }
            }

    def createContext(self, object_: Dict[str, Any]) -> None:
        """Create the context for the given object."""
        if isinstance(object_, HydraClass):
            self.add(object_.title, object_.id)
            for prop in object_.supportedProperty:
                self.add(prop.title, self.prop)
        if isinstance(object_, HydraCollection):
            self.add(object_.name, "vocab:{}".format(object_.name))
            self.add(object_.class_.title, object_.class_.id)

    def generate(self) -> Dict[str, Any]:
        """Get as a python dict."""
        return self.context

    def add(self, key: str, value: Union[Dict[str, str], str]) -> None:
        """Add entry to context."""
        self.context[key] = value
