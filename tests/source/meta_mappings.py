# Auto generated from .yaml by pythongen.py version:
# Generation date:
# Schema: testMetamodelMappings
#
# id: http://example.org/mappings/
# description: Mappings test
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef


metamodel_version = "1.4.2"


# Namespaces
EX = Namespace('http://example.org/mappings/')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = EX


# Types
class String(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = EX.String


class IdentifierType(String):
    """ A string that is intended to uniquely identify a thing May be URI in full or compact (CURIE) form """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "identifier type"
    type_model_uri = EX.IdentifierType


# Class references
class C1S2(IdentifierType):
    pass


class C2S2(C1S2):
    pass


class C3S2(C1S2):
    pass


@dataclass
class C1(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.C1
    class_class_curie: ClassVar[str] = "ex:C1"
    class_name: ClassVar[str] = "c1"
    class_model_uri: ClassVar[URIRef] = EX.C1

    s2: Union[str, C1S2]
    s1: Optional[str] = None

    def __post_init__(self):
        if self.s2 is None:
            raise ValueError(f"s2 must be supplied")
        if not isinstance(self.s2, C1S2):
            self.s2 = C1S2(self.s2)
        super().__post_init__()


@dataclass
class C2(C1):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.C2
    class_class_curie: ClassVar[str] = "ex:C2"
    class_name: ClassVar[str] = "c2"
    class_model_uri: ClassVar[URIRef] = EX.C2

    s2: Union[str, C2S2] = None

    def __post_init__(self):
        if self.s2 is None:
            raise ValueError(f"s2 must be supplied")
        if not isinstance(self.s2, C2S2):
            self.s2 = C2S2(self.s2)
        super().__post_init__()


@dataclass
class C3(C1):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.C3
    class_class_curie: ClassVar[str] = "ex:C3"
    class_name: ClassVar[str] = "c3"
    class_model_uri: ClassVar[URIRef] = EX.C3

    s2: Union[str, C3S2] = None

    def __post_init__(self):
        if self.s2 is None:
            raise ValueError(f"s2 must be supplied")
        if not isinstance(self.s2, C3S2):
            self.s2 = C3S2(self.s2)
        super().__post_init__()
