# Auto generated from uriandcurie.yaml by pythongen.py version: 0.3.0
# Generation date: 2019-10-23 11:50
# Schema: uriandcurie
#
# id: http://example.org/test/uriandcurie
# description:
# license:

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from biolinkml.utils.metamodelcore import Curie, ElementIdentifier, NCName, NodeIdentifier, URI, URIorCURIE

metamodel_version = "1.4.3"


# Namespaces
M = CurieNamespace('m', 'http://example.org/test/uriandcurie')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = M


# Types
class String(str):
    """ A character string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = M.String


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = M.Uriorcurie


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = M.Uri


class Curie(Curie):
    """ a CURIE """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "curie"
    type_model_uri = M.Curie


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = M.Ncname


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX.iri
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = M.Objectidentifier


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX.nonliteral
    type_class_curie = "shex:nonliteral"
    type_name = "nodeidentifier"
    type_model_uri = M.Nodeidentifier


# Class references
class C1Id(ElementIdentifier):
    pass


@dataclass
class C1(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = M.C1
    class_class_curie: ClassVar[str] = "m:C1"
    class_name: ClassVar[str] = "c1"
    class_model_uri: ClassVar[URIRef] = M.C1

    id: Union[str, C1Id]
    hasCurie: Optional[Union[str, Curie]] = None
    hasURI: Optional[Union[str, URI]] = None
    hasNcName: Optional[Union[str, NCName]] = None
    id2: Optional[Union[str, NodeIdentifier]] = None

    def __post_init__(self):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, C1Id):
            self.id = C1Id(self.id)
        if self.hasCurie is not None and not isinstance(self.hasCurie, Curie):
            self.hasCurie = Curie(self.hasCurie)
        if self.hasURI is not None and not isinstance(self.hasURI, URI):
            self.hasURI = URI(self.hasURI)
        if self.hasNcName is not None and not isinstance(self.hasNcName, NCName):
            self.hasNcName = NCName(self.hasNcName)
        if self.id2 is not None and not isinstance(self.id2, NodeIdentifier):
            self.id2 = NodeIdentifier(self.id2)
        super().__post_init__()