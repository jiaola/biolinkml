
# Type: chemical to chemical association


A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.

URI: [biolink:ChemicalToChemicalAssociation](https://w3id.org/biolink/vocab/ChemicalToChemicalAssociation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[ChemicalToChemicalAssociation|relation(i):uriorcurie;id(i):nodeidentifier;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[ChemicalToChemicalAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[ChemicalToChemicalAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[ChemicalToChemicalAssociation],%20\[NamedThing]<subject(i)%201..1-%20\[ChemicalToChemicalAssociation],%20\[ChemicalSubstance]<object%201..1-%20\[ChemicalToChemicalAssociation],%20\[ChemicalToChemicalAssociation]uses%20-.->\[ChemicalToThingAssociation],%20\[ChemicalToChemicalAssociation]^-\[ChemicalToChemicalDerivationAssociation],%20\[Association]^-\[ChemicalToChemicalAssociation])

## Parents

 *  is_a: [association](association.md) - A typed association between two entities, supported by evidence

## Uses Mixins

 *  mixin: [chemical to thing association](chemical to thing association.md) - An interaction between a chemical entity and another entity

## Children

 * [chemical to chemical derivation association](chemical to chemical derivation association.md) - A causal relationship between two chemical entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction:

## Referenced by class


## Attributes


### Own

 * [chemical to chemical association➞object](chemical_to_chemical_association_object.md)  <sub>REQ</sub>
    * range: [chemical substance](chemical substance.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [named thing](named thing.md)
    * inherited from: [association](association.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [Uriorcurie](type/Uriorcurie.md)
    * inherited from: [association](association.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [named thing](named thing.md)
    * inherited from: [association](association.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [Nodeidentifier](type/Nodeidentifier.md)
    * inherited from: [association](association.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](type/Boolean.md)
    * inherited from: [association](association.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [ontology class](ontology class.md)
    * inherited from: [association](association.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [ontology class](ontology class.md)
    * inherited from: [association](association.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [publication](publication.md)
    * inherited from: [association](association.md)
 * [provided by](provided_by.md)  <sub>OPT</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [provider](provider.md)
    * inherited from: [association](association.md)

### Domain for slot:

 * [chemical to chemical association➞object](chemical_to_chemical_association_object.md)  <sub>REQ</sub>
    * range: [chemical substance](chemical substance.md)