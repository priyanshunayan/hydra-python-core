"""Generated API Documentation sample using doc_writer_sample.py."""
    
doc = {
    "@context": {
        "ApiDocumentation": "hydra:ApiDocumentation",
        "description": "hydra:description",
        "domain": {
            "@id": "rdfs:domain",
            "@type": "@id"
        },
        "entrypoint": {
            "@id": "hydra:entrypoint",
            "@type": "@id"
        },
        "expects": {
            "@id": "hydra:expects",
            "@type": "@id"
        },
        "expectsHeader": "hydra:expectsHeader",
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "label": "rdfs:label",
        "manages": "hydra:manages",
        "method": "hydra:method",
        "object": {
            "@id": "hydra:object",
            "@type": "@id"
        },
        "possibleStatus": "hydra:possibleStatus",
        "property": {
            "@id": "hydra:property",
            "@type": "@id"
        },
        "range": {
            "@id": "rdfs:range",
            "@type": "@id"
        },
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "readable": "hydra:readable",
        "required": "hydra:required",
        "returns": {
            "@id": "hydra:returns",
            "@type": "@id"
        },
        "returnsHeader": "hydra:returnsHeader",
        "search": "hydra:search",
        "statusCode": "hydra:statusCode",
        "subClassOf": {
            "@id": "rdfs:subClassOf",
            "@type": "@id"
        },
        "subject": {
            "@id": "hydra:subject",
            "@type": "@id"
        },
        "supportedClass": "hydra:supportedClass",
        "supportedOperation": "hydra:supportedOperation",
        "supportedProperty": "hydra:supportedProperty",
        "title": "hydra:title",
        "writeable": "hydra:writeable"
    },
    "@id": "https://hydrus.com/api/vocab",
    "@type": "ApiDocumentation",
    "description": "Description for the API Documentation",
    "entrypoint": "https://hydrus.com/api",
    "possibleStatus": [],
    "supportedClass": [
        {
            "@id": "https://hydrus.com/api/vocab#dummyClass",
            "@type": "hydra:Class",
            "description": "A dummyClass for demo",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "https://hydrus.com/api/vocab#dummyClass",
                    "expectsHeader": [],
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "dummyClass updated.",
                            "statusCode": 200,
                            "title": ""
                        }
                    ],
                    "returns": "null",
                    "returnsHeader": [
                        "Content-Type",
                        "Content-Length"
                    ],
                    "title": "UpdateClass"
                },
                {
                    "@type": "http://schema.org/DeleteAction",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "DELETE",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "dummyClass deleted.",
                            "statusCode": 200,
                            "title": ""
                        }
                    ],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "DeleteClass"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "https://hydrus.com/api/vocab#dummyClass",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "dummyClass successfully added.",
                            "statusCode": 201,
                            "title": ""
                        }
                    ],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "AddClass"
                },
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "dummyClass returned.",
                            "statusCode": 200,
                            "title": ""
                        }
                    ],
                    "returns": "https://hydrus.com/api/vocab#dummyClass",
                    "returnsHeader": [],
                    "title": "GetClass"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://props.hydrus.com/prop1",
                    "readable": "false",
                    "required": "false",
                    "title": "Prop1",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://props.hydrus.com/prop1",
                    "readable": "false",
                    "required": "false",
                    "title": "Prop2",
                    "writeable": "true"
                }
            ],
            "title": "dummyClass"
        },
        {
            "@id": "https://hydrus.com/api/vocab#extraClass",
            "@type": "hydra:Class",
            "description": "Class without any explicit methods",
            "supportedOperation": [],
            "supportedProperty": [],
            "title": "extraClass"
        },
        {
            "@id": "https://hydrus.com/api/vocab#singleClass",
            "@type": "hydra:Class",
            "description": "A non collection class",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "https://hydrus.com/api/vocab#singleClass",
                    "expectsHeader": [],
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "singleClass changed.",
                            "statusCode": 200,
                            "title": ""
                        }
                    ],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "UpdateClass"
                },
                {
                    "@type": "http://schema.org/DeleteAction",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "DELETE",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "singleClass deleted.",
                            "statusCode": 200,
                            "title": ""
                        }
                    ],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "DeleteClass"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "https://hydrus.com/api/vocab#singleClass",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "singleClass successfully added.",
                            "statusCode": 201,
                            "title": ""
                        }
                    ],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "AddClass"
                },
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "singleClass returned.",
                            "statusCode": 200,
                            "title": ""
                        }
                    ],
                    "returns": "https://hydrus.com/api/vocab#singleClass",
                    "returnsHeader": [],
                    "title": "GetClass"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://props.hydrus.com/prop1",
                    "readable": "false",
                    "required": "false",
                    "title": "Prop1",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://props.hydrus.com/prop1",
                    "readable": "false",
                    "required": "false",
                    "title": "Prop2",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": {
                        "@id": "https://hydrus.com/api/vocab#singleClass/dummyProp",
                        "@type": "hydra:Link",
                        "description": "",
                        "domain": "https://hydrus.com/api/vocab#singleClass",
                        "range": "https://hydrus.com/api/vocab#dummyClass",
                        "supportedOperation": [],
                        "title": "dummyProp"
                    },
                    "readable": "false",
                    "required": "false",
                    "title": "dummyProp",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://hydrus.com/api/vocab#anotherSingleClass",
                    "readable": "false",
                    "required": "false",
                    "title": "singleClassProp",
                    "writeable": "true"
                }
            ],
            "title": "singleClass"
        },
        {
            "@id": "https://hydrus.com/api/vocab#anotherSingleClass",
            "@type": "hydra:Class",
            "description": "An another non collection class",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "anotherSingleClass returned.",
                            "statusCode": 200,
                            "title": ""
                        }
                    ],
                    "returns": "https://hydrus.com/api/vocab#anotherSingleClass",
                    "returnsHeader": [],
                    "title": "GetClass"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://props.hydrus.com/prop1",
                    "readable": "false",
                    "required": "false",
                    "title": "Prop1",
                    "writeable": "true"
                }
            ],
            "title": "anotherSingleClass"
        },
        {
            "@id": "https://hydrus.com/api/vocab#http://www.w3.org/ns/hydra/core#Resource",
            "@type": "hydra:Class",
            "description": "Resource",
            "supportedOperation": [],
            "supportedProperty": [],
            "title": "http://www.w3.org/ns/hydra/core#Resource"
        },
        {
            "@id": "https://hydrus.com/api/vocab#http://www.w3.org/ns/hydra/core#Collection",
            "@type": "hydra:Class",
            "description": "Collection",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "false",
                    "required": "null",
                    "title": "members",
                    "writeable": "false"
                }
            ],
            "title": "http://www.w3.org/ns/hydra/core#Collection"
        },
        {
            "@id": "https://hydrus.com/api/vocab#Extraclasses",
            "@type": "Collection",
            "description": "This collection comprises of instances of ExtraClass",
            "manages": {
                "object": "https://hydrus.com/api/vocab#extraClass",
                "property": "rdf:type"
            },
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "https://hydrus.com/api/vocab#Extraclasses_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all the members of Extraclasses",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "https://hydrus.com/api/vocab#extraClass",
                    "returnsHeader": []
                },
                {
                    "@id": "https://hydrus.com/api/vocab#Extraclasses_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new member in Extraclasses",
                    "expects": "https://hydrus.com/api/vocab#extraClass",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "A new member in Extraclasses created",
                            "statusCode": 201,
                            "title": ""
                        }
                    ],
                    "returns": "https://hydrus.com/api/vocab#extraClass",
                    "returnsHeader": []
                },
                {
                    "@id": "https://hydrus.com/api/vocab#Extraclasses_update",
                    "@type": "http://schema.org/UpdateAction",
                    "description": "Update member of  Extraclasses ",
                    "expects": "https://hydrus.com/api/vocab#extraClass",
                    "expectsHeader": [],
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "If the entity was updatedfrom Extraclasses.",
                            "statusCode": 200,
                            "title": ""
                        }
                    ],
                    "returns": "https://hydrus.com/api/vocab#extraClass",
                    "returnsHeader": []
                },
                {
                    "@id": "https://hydrus.com/api/vocab#Extraclasses_delete",
                    "@type": "http://schema.org/DeleteAction",
                    "description": "Delete member of Extraclasses ",
                    "expects": "https://hydrus.com/api/vocab#extraClass",
                    "expectsHeader": [],
                    "method": "DELETE",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "If entity was deletedsuccessfully from Extraclasses.",
                            "statusCode": 200,
                            "title": ""
                        }
                    ],
                    "returns": "https://hydrus.com/api/vocab#extraClass",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The members of Extraclasses",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "false",
                    "required": "false",
                    "title": "members",
                    "writeable": "false"
                }
            ],
            "title": "Extraclasses"
        },
        {
            "@id": "https://hydrus.com/api/vocab#dummyclasses",
            "@type": "Collection",
            "description": "This collection comprises of instances of dummyClass",
            "manages": {
                "object": "https://hydrus.com/api/vocab#dummyClass",
                "property": "rdf:type"
            },
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "https://hydrus.com/api/vocab#dummyclasses_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all the members of dummyclasses",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "https://hydrus.com/api/vocab#dummyClass",
                    "returnsHeader": []
                },
                {
                    "@id": "https://hydrus.com/api/vocab#dummyclasses_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new member in dummyclasses",
                    "expects": "https://hydrus.com/api/vocab#dummyClass",
                    "expectsHeader": [],
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "A new member in dummyclasses created",
                            "statusCode": 201,
                            "title": ""
                        }
                    ],
                    "returns": "https://hydrus.com/api/vocab#dummyClass",
                    "returnsHeader": []
                },
                {
                    "@id": "https://hydrus.com/api/vocab#dummyclasses_update",
                    "@type": "http://schema.org/UpdateAction",
                    "description": "Update member of  dummyclasses ",
                    "expects": "https://hydrus.com/api/vocab#dummyClass",
                    "expectsHeader": [],
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "If the entity was updatedfrom dummyclasses.",
                            "statusCode": 200,
                            "title": ""
                        }
                    ],
                    "returns": "https://hydrus.com/api/vocab#dummyClass",
                    "returnsHeader": []
                },
                {
                    "@id": "https://hydrus.com/api/vocab#dummyclasses_delete",
                    "@type": "http://schema.org/DeleteAction",
                    "description": "Delete member of dummyclasses ",
                    "expects": "https://hydrus.com/api/vocab#dummyClass",
                    "expectsHeader": [],
                    "method": "DELETE",
                    "possibleStatus": [
                        {
                            "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                            "@type": "Status",
                            "description": "If entity was deletedsuccessfully from dummyclasses.",
                            "statusCode": 200,
                            "title": ""
                        }
                    ],
                    "returns": "https://hydrus.com/api/vocab#dummyClass",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The members of dummyclasses",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "false",
                    "required": "false",
                    "title": "members",
                    "writeable": "false"
                }
            ],
            "title": "dummyclasses"
        },
        {
            "@id": "EntryPoint",
            "@type": "hydra:Class",
            "description": "EntryPoint",
            "supportedOperation": [
                {
                    "@id": "https://hydrus.comentry_point",
                    "@type": "EntryPoint",
                    "description": "The APIs main entry point.",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "hydra:description": "The singleClass Class",
                    "hydra:title": "singleclass",
                    "property": {
                        "@id": "https://hydrus.com/api/vocab#EntryPoint/singleClass",
                        "@type": "hydra:Link",
                        "description": "A non collection class",
                        "domain": "https://hydrus.com/api/vocab#EntryPoint",
                        "label": "singleClass",
                        "range": "https://hydrus.com/api/vocab#singleClass",
                        "supportedOperation": [
                            {
                                "@id": "updateclass",
                                "@type": "http://schema.org/UpdateAction",
                                "description": "null",
                                "expects": "https://hydrus.com/api/vocab#singleClass",
                                "expectsHeader": [],
                                "label": "UpdateClass",
                                "method": "POST",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "singleClass changed.",
                                        "statusCode": 200,
                                        "title": ""
                                    }
                                ],
                                "returns": "null",
                                "returnsHeader": []
                            },
                            {
                                "@id": "deleteclass",
                                "@type": "http://schema.org/DeleteAction",
                                "description": "null",
                                "expects": "null",
                                "expectsHeader": [],
                                "label": "DeleteClass",
                                "method": "DELETE",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "singleClass deleted.",
                                        "statusCode": 200,
                                        "title": ""
                                    }
                                ],
                                "returns": "null",
                                "returnsHeader": []
                            },
                            {
                                "@id": "addclass",
                                "@type": "http://schema.org/AddAction",
                                "description": "null",
                                "expects": "https://hydrus.com/api/vocab#singleClass",
                                "expectsHeader": [],
                                "label": "AddClass",
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "singleClass successfully added.",
                                        "statusCode": 201,
                                        "title": ""
                                    }
                                ],
                                "returns": "null",
                                "returnsHeader": []
                            },
                            {
                                "@id": "getclass",
                                "@type": "http://schema.org/FindAction",
                                "description": "null",
                                "expects": "null",
                                "expectsHeader": [],
                                "label": "GetClass",
                                "method": "GET",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "singleClass returned.",
                                        "statusCode": 200,
                                        "title": ""
                                    }
                                ],
                                "returns": "https://hydrus.com/api/vocab#singleClass",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": "true",
                    "required": "null",
                    "writeable": "false"
                },
                {
                    "hydra:description": "The anotherSingleClass Class",
                    "hydra:title": "anothersingleclass",
                    "property": {
                        "@id": "https://hydrus.com/api/vocab#EntryPoint/anotherSingleClass",
                        "@type": "hydra:Link",
                        "description": "An another non collection class",
                        "domain": "https://hydrus.com/api/vocab#EntryPoint",
                        "label": "anotherSingleClass",
                        "range": "https://hydrus.com/api/vocab#anotherSingleClass",
                        "supportedOperation": [
                            {
                                "@id": "getclass",
                                "@type": "http://schema.org/FindAction",
                                "description": "null",
                                "expects": "null",
                                "expectsHeader": [],
                                "label": "GetClass",
                                "method": "GET",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "anotherSingleClass returned.",
                                        "statusCode": 200,
                                        "title": ""
                                    }
                                ],
                                "returns": "https://hydrus.com/api/vocab#anotherSingleClass",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": "true",
                    "required": "null",
                    "writeable": "false"
                },
                {
                    "hydra:description": "The Extraclasses collection",
                    "hydra:title": "extraclasses",
                    "property": {
                        "@id": "https://hydrus.com/api/vocab#EntryPoint/EcTest",
                        "@type": "hydra:Link",
                        "description": "The Extraclasses collection",
                        "domain": "https://hydrus.com/api/vocab#EntryPoint",
                        "label": "Extraclasses",
                        "range": "https://hydrus.com/api/vocab#:Extraclasses",
                        "supportedOperation": [
                            {
                                "@id": "https://hydrus.com/api/vocab#extraclasses_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all the members of Extraclasses",
                                "expects": "null",
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "https://hydrus.com/api/vocab#extraClass",
                                "returnsHeader": []
                            },
                            {
                                "@id": "https://hydrus.com/api/vocab#extraclasses_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new member in Extraclasses",
                                "expects": "https://hydrus.com/api/vocab#extraClass",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "A new member in Extraclasses created",
                                        "statusCode": 201,
                                        "title": ""
                                    }
                                ],
                                "returns": "https://hydrus.com/api/vocab#extraClass",
                                "returnsHeader": []
                            },
                            {
                                "@id": "https://hydrus.com/api/vocab#extraclasses_update",
                                "@type": "http://schema.org/UpdateAction",
                                "description": "Update member of  Extraclasses ",
                                "expects": "https://hydrus.com/api/vocab#extraClass",
                                "expectsHeader": [],
                                "method": "POST",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "If the entity was updatedfrom Extraclasses.",
                                        "statusCode": 200,
                                        "title": ""
                                    }
                                ],
                                "returns": "https://hydrus.com/api/vocab#extraClass",
                                "returnsHeader": []
                            },
                            {
                                "@id": "https://hydrus.com/api/vocab#extraclasses_delete",
                                "@type": "http://schema.org/DeleteAction",
                                "description": "Delete member of Extraclasses ",
                                "expects": "https://hydrus.com/api/vocab#extraClass",
                                "expectsHeader": [],
                                "method": "DELETE",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "If entity was deletedsuccessfully from Extraclasses.",
                                        "statusCode": 200,
                                        "title": ""
                                    }
                                ],
                                "returns": "https://hydrus.com/api/vocab#extraClass",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": "true",
                    "required": "null",
                    "writeable": "false"
                },
                {
                    "hydra:description": "The dummyclasses collection",
                    "hydra:title": "dummyclasses",
                    "property": {
                        "@id": "https://hydrus.com/api/vocab#EntryPoint/DcTest",
                        "@type": "hydra:Link",
                        "description": "The dummyclasses collection",
                        "domain": "https://hydrus.com/api/vocab#EntryPoint",
                        "label": "dummyclasses",
                        "range": "https://hydrus.com/api/vocab#:dummyclasses",
                        "supportedOperation": [
                            {
                                "@id": "https://hydrus.com/api/vocab#dummyclasses_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all the members of dummyclasses",
                                "expects": "null",
                                "expectsHeader": [],
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "https://hydrus.com/api/vocab#dummyClass",
                                "returnsHeader": []
                            },
                            {
                                "@id": "https://hydrus.com/api/vocab#dummyclasses_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new member in dummyclasses",
                                "expects": "https://hydrus.com/api/vocab#dummyClass",
                                "expectsHeader": [],
                                "method": "PUT",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "A new member in dummyclasses created",
                                        "statusCode": 201,
                                        "title": ""
                                    }
                                ],
                                "returns": "https://hydrus.com/api/vocab#dummyClass",
                                "returnsHeader": []
                            },
                            {
                                "@id": "https://hydrus.com/api/vocab#dummyclasses_update",
                                "@type": "http://schema.org/UpdateAction",
                                "description": "Update member of  dummyclasses ",
                                "expects": "https://hydrus.com/api/vocab#dummyClass",
                                "expectsHeader": [],
                                "method": "POST",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "If the entity was updatedfrom dummyclasses.",
                                        "statusCode": 200,
                                        "title": ""
                                    }
                                ],
                                "returns": "https://hydrus.com/api/vocab#dummyClass",
                                "returnsHeader": []
                            },
                            {
                                "@id": "https://hydrus.com/api/vocab#dummyclasses_delete",
                                "@type": "http://schema.org/DeleteAction",
                                "description": "Delete member of dummyclasses ",
                                "expects": "https://hydrus.com/api/vocab#dummyClass",
                                "expectsHeader": [],
                                "method": "DELETE",
                                "possibleStatus": [
                                    {
                                        "@context": "http://www.w3.org/ns/hydra/context.jsonld",
                                        "@type": "Status",
                                        "description": "If entity was deletedsuccessfully from dummyclasses.",
                                        "statusCode": 200,
                                        "title": ""
                                    }
                                ],
                                "returns": "https://hydrus.com/api/vocab#dummyClass",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": "true",
                    "required": "null",
                    "writeable": "false"
                }
            ],
            "title": "EntryPoint"
        }
    ],
    "title": "Title for the API Documentation"
}
