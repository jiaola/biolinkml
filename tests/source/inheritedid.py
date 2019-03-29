# id: https://example.org/inheritedid
# description: Test
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.metamodelcore import URI

metamodel_version = "1.2.0"

inherited_slots: List[str] = []


# Types
class String(str):
    pass


class Uri(URI):
    """ a complete URI """
    pass


class IdentifierType(String):
    """ A string that is intended to uniquely identify a thing May be URI in full or compact (CURIE) form """
    pass


class LabelType(String):
    """ A string that provides a human-readable name for a thing """
    pass


# Class references
class NamedThingId(IdentifierType):
    pass


class AttributeId(IdentifierType):
    pass


class BiologicalSexId(AttributeId):
    pass


class OntologyClassId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """

    # === named thing ===
    id: Union[str, NamedThingId]
    name: Optional[Union[str, LabelType]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)
        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)


@dataclass
class Attribute(YAMLRoot):
    """
    A property or characteristic of an entity
    """

    # === attribute ===
    id: Union[str, AttributeId]
    name: Optional[Union[str, LabelType]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.id, AttributeId):
            self.id = AttributeId(self.id)
        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)


@dataclass
class BiologicalSex(Attribute):

    # === attribute ===
    id: Union[str, BiologicalSexId] = None
    name: Optional[Union[str, LabelType]] = None

    # === biological sex ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, BiologicalSexId):
            self.id = BiologicalSexId(self.id)


@dataclass
class OntologyClass(NamedThing):
    """
    a concept or class in an ontology, vocabulary or thesaurus
    """

    # === named thing ===
    id: Union[str, OntologyClassId] = None
    name: Optional[Union[str, LabelType]] = None

    # === ontology class ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)