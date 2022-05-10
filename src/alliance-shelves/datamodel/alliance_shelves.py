# Auto generated from alliance_shelves.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-05-10T09:05:36
# Schema: alliance-shelves
#
# id: https://w3id.org/my_org/alliance-shelves
# description: Enter a detailed description of your project here
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
ALLIANCE_SHELVES = CurieNamespace('alliance-shelves', 'https://w3id.org/my_org/alliance-shelves')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
FAMREL = CurieNamespace('famrel', 'http://example.org/famrel/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
ULINE = CurieNamespace('uline', 'http://example.org/UNKNOWN/uline/')
DEFAULT_ = ALLIANCE-SHELVES


# Types

# Class references



@dataclass
class Furniture(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE-SHELVES.Furniture
    class_class_curie: ClassVar[str] = "alliance-shelves:Furniture"
    class_name: ClassVar[str] = "Furniture"
    class_model_uri: ClassVar[URIRef] = ALLIANCE-SHELVES.Furniture

    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    color: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.image is not None and not isinstance(self.image, str):
            self.image = str(self.image)

        if self.color is not None and not isinstance(self.color, str):
            self.color = str(self.color)

        super().__post_init__(**kwargs)


@dataclass
class Shelf(Furniture):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE-SHELVES.Shelf
    class_class_curie: ClassVar[str] = "alliance-shelves:Shelf"
    class_name: ClassVar[str] = "Shelf"
    class_model_uri: ClassVar[URIRef] = ALLIANCE-SHELVES.Shelf

    height: Optional[int] = None
    width: Optional[str] = None
    number_of_shelves: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.height is not None and not isinstance(self.height, int):
            self.height = int(self.height)

        if self.width is not None and not isinstance(self.width, str):
            self.width = str(self.width)

        if self.number_of_shelves is not None and not isinstance(self.number_of_shelves, str):
            self.number_of_shelves = str(self.number_of_shelves)

        super().__post_init__(**kwargs)


class KitchenTable(Furniture):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE-SHELVES.KitchenTable
    class_class_curie: ClassVar[str] = "alliance-shelves:KitchenTable"
    class_name: ClassVar[str] = "KitchenTable"
    class_model_uri: ClassVar[URIRef] = ALLIANCE-SHELVES.KitchenTable


@dataclass
class Couch(Furniture):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE-SHELVES.Couch
    class_class_curie: ClassVar[str] = "alliance-shelves:Couch"
    class_name: ClassVar[str] = "Couch"
    class_model_uri: ClassVar[URIRef] = ALLIANCE-SHELVES.Couch

    color: Union[str, "CouchColorEnumeration"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.color):
            self.MissingRequiredField("color")
        if not isinstance(self.color, CouchColorEnumeration):
            self.color = CouchColorEnumeration(self.color)

        super().__post_init__(**kwargs)


# Enumerations
class CouchColorEnumeration(EnumDefinitionImpl):

    black = PermissibleValue(text="black",
                                 meaning=PATO["0000317"])
    blue = PermissibleValue(text="blue")
    red = PermissibleValue(text="red")

    _defn = EnumDefinition(
        name="CouchColorEnumeration",
    )

# Slots
class slots:
    pass

slots.color = Slot(uri=ALLIANCE-SHELVES.color, name="color", curie=ALLIANCE-SHELVES.curie('color'),
                   model_uri=ALLIANCE-SHELVES.color, domain=None, range=Optional[str])

slots.height = Slot(uri=ALLIANCE-SHELVES.height, name="height", curie=ALLIANCE-SHELVES.curie('height'),
                   model_uri=ALLIANCE-SHELVES.height, domain=None, range=Optional[int])

slots.width = Slot(uri=ALLIANCE-SHELVES.width, name="width", curie=ALLIANCE-SHELVES.curie('width'),
                   model_uri=ALLIANCE-SHELVES.width, domain=None, range=Optional[str])

slots.number_of_shelves = Slot(uri=ALLIANCE-SHELVES.number_of_shelves, name="number_of_shelves", curie=ALLIANCE-SHELVES.curie('number_of_shelves'),
                   model_uri=ALLIANCE-SHELVES.number_of_shelves, domain=None, range=Optional[str])

slots.id = Slot(uri=ALLIANCE-SHELVES.id, name="id", curie=ALLIANCE-SHELVES.curie('id'),
                   model_uri=ALLIANCE-SHELVES.id, domain=None, range=Optional[str])

slots.name = Slot(uri=ALLIANCE-SHELVES.name, name="name", curie=ALLIANCE-SHELVES.curie('name'),
                   model_uri=ALLIANCE-SHELVES.name, domain=None, range=Optional[str])

slots.description = Slot(uri=ALLIANCE-SHELVES.description, name="description", curie=ALLIANCE-SHELVES.curie('description'),
                   model_uri=ALLIANCE-SHELVES.description, domain=None, range=Optional[str])

slots.image = Slot(uri=ALLIANCE-SHELVES.image, name="image", curie=ALLIANCE-SHELVES.curie('image'),
                   model_uri=ALLIANCE-SHELVES.image, domain=None, range=Optional[str])

slots.Couch_color = Slot(uri=ALLIANCE-SHELVES.color, name="Couch_color", curie=ALLIANCE-SHELVES.curie('color'),
                   model_uri=ALLIANCE-SHELVES.Couch_color, domain=Couch, range=Union[str, "CouchColorEnumeration"])