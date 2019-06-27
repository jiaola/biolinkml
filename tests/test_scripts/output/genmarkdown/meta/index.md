# Metamodel schema


A metamodel for defining biolink related schemas

### Classes

 * [AltDescription](AltDescription.md) - an attributed description
 * [Element](Element.md) - a named element in the model
    * [Definition](Definition.md) - base class for definitions
       * [ClassDefinition](ClassDefinition.md) - the definition of a class or interface
       * [SlotDefinition](SlotDefinition.md) - the definition of a property or a slot
    * [SchemaDefinition](SchemaDefinition.md) - a collection of subset, type, slot and class definitions
    * [SubsetDefinition](SubsetDefinition.md) - the name and description of a subset
    * [TypeDefinition](TypeDefinition.md) - A data type definition.
 * [Example](Example.md) - usage example and description
 * [LocalName](LocalName.md) - an attributed label
 * [Prefix](Prefix.md) - prefix URI tuple
### Mixins

### Slots

 * [abstract](abstract.md) - an abstract class is a high level class or slot that is typically used to group common slots together and cannot be directly instantiated.
 * [alias](alias.md) - the name used for a slot in the context of its owning class.  If present, this is used instead of the actual slot name.
 * [aliases](aliases.md)
 * [source](alt_description_source.md) - the source of an attributed description
 * [description](alt_description_text.md) - text of an attributed description
 * [alt_descriptions](alt_descriptions.md)
 * [apply_to](apply_to.md) - Used to extend class or slot definitions. For example, if we have a core schema where a gene has two slots for identifier and symbol, and we have a specialized schema for my_organism where we wish to add a slot systematic_name, we can avoid subclassing by defining a class gene_my_organism, adding the slot to this class, and then adding an apply_to pointing to the gene class. The new slot will be 'injected into' the gene class.
    * [apply_to](class_definition_apply_to.md)
    * [apply_to](slot_definition_apply_to.md)
 * [base](base.md) - python base type that implements this type definition
 * [class_uri](class_uri.md) - URI of the class in an RDF environment
 * [classes](classes.md) - class definitions
 * [comments](comments.md) - notes and comments about an element intended for external consumption
 * [default_curi_maps](default_curi_maps.md) - ordered list of prefixcommon biocontexts to be fetched to resolve id prefixes and inline prefix variables
 * [default_prefix](default_prefix.md) - default and base prefix -- used for ':' identifiers, @base and @vocab
 * [default_range](default_range.md) - default slot range to be used if range element is omitted from a slot definition
 * [defining_slots](defining_slots.md) - The combination of is a plus defining slots form a genus-differentia definition, or the set of necessary and sufficient conditions that can be transformed into an OWL equivalence axiom
 * [deprecated](deprecated.md) - Description of why and when this element will no longer be used
 * [description](description.md) - a description of the element's purpose and use
 * [domain](domain.md) - defines the type of the subject of the slot.  Given the following slot definition
 * [emit_prefixes](emit_prefixes.md) - a list of Curie prefixes that are used in the representation of instances of the model.  All prefixes in this list are added to the prefix sections of the target models.
 * [examples](examples.md) - example usages of an element
 * [from_schema](from_schema.md) - id of the schema that defined the element
 * [generation_date](generation_date.md) - date and time that the schema was loaded/generated
 * [id](id.md) - The official schema URI
 * [id_prefixes](id_prefixes.md) - the identifier of this class or slot must begin with one of the URIs referenced by this prefix
 * [identifier](identifier.md) - true means that this slot is the subject of a set of assertions.  Identifiers do not appear as predicates in the model
 * [ifabsent](ifabsent.md) - description of special behavior if the slot is absent
 * [imported_from](imported_from.md) - the imports entry that this element was derived from.  Empty means primary source
 * [imports](imports.md) - other schemas that are included in this schema
 * [in_subset](in_subset.md) - used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)
 * [inherited](inherited.md) - true means that the *value* of a slot is inherited by subclasses
 * [inlined](inlined.md) - an inlined definition a list of actual values rather than references.  Only applies to slots whose range is a class.
 * [inverse](inverse.md) - indicates that any instance of d s r implies that there is also an instance of r s' d
 * [is_a](is_a.md) - specifies single-inheritance between classes or slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is a and mixins are recursively unfolded
    * [is_a](class_definition_is_a.md)
    * [is_a](slot_definition_is_a.md)
 * [is_class_field](is_class_field.md) - indicates that any instance, i,  the domain of this slot will include an assert of i s range
 * [is_usage_slot](is_usage_slot.md) - True means that this slot was defined in a slot_usage situation
 * [key](key.md) - true means that the slot uniquely identifies the element within the context of its container.  Key slots are NOT identifiers - they do not serve as subjects
 * [license](license.md) - license for the schema
 * [local_name_source](local_name_source.md) - the ncname of the source of the name
 * [local_name_value](local_name_value.md) - a name assigned to an element in a given ontology
 * [local_names](local_names.md)
 * [mappings](mappings.md) - A list of terms from different schemas or terminology systems that have comparable meaning. These may include terms that are precisely equivalent, broader or narrower in meaning, or otherwise semantically related but not equivalent from a strict ontological perspective.
 * [metamodel_version](metamodel_version.md) - Version of the metamodel used to load the schema
 * [mixin](mixin.md) - this slot or class can only be used as a mixin -- equivalent to abstract
 * [mixins](mixins.md) - List of definitions to be mixed in. Targets may be any definition of the same type
    * [mixins](class_definition_mixins.md)
    * [mixins](slot_definition_mixins.md)
 * [multivalued](multivalued.md) - true means that slot can have more than one value
 * [name](name.md) - the unique name of the element within the context of the schema.  Name is combined with the default prefix to form the globally unique subject of the target class.
 * [notes](notes.md) - editorial notes about an element intended for internal consumption
 * [owner](owner.md) - the "owner" of the slot. It is the class if it appears in the slots list, otherwise the declaring slot
 * [prefix_prefix](prefix_prefix.md) - the nsname (sans ':' for a given prefix)
 * [prefix_reference](prefix_reference.md) - A URI associated with a given prefix
 * [prefixes](prefixes.md) - prefix / URI definitions to be added to the context beyond those fetched from prefixcommons in id prefixes
 * [range](range.md) - defines the type of the object of the slot.  Given the following slot definition
 * [readonly](readonly.md) - If present, slot is read only.  Text explains why
 * [repr](repr.md) - the name of the python object that implements this type definition
 * [required](required.md) - true means that the slot must be present in the loaded definition
 * [role](role.md) - the role played by the slot range
 * [see_also](see_also.md) - a reference
 * [singular_name](singular_name.md) - a name that is used in the singular form
 * [slots](slot_definitions.md) - slot definitions
 * [slot_uri](slot_uri.md) - predicate of this slot for semantic web application
 * [slot_usage](slot_usage.md) - the redefinition of a slot in the context of the containing class definition.
 * [slots](slots.md) - list of slot names that are applicable to a class
 * [source_file](source_file.md) - name, uri or description of the source of the schema
 * [source_file_date](source_file_date.md) - modification date of the source of the schema
 * [source_file_size](source_file_size.md) - size in bytes of the source of the schema
 * [subclass_of](subclass_of.md) - rdfs:subClassOf to be emitted in OWL generation
 * [subproperty_of](subproperty_of.md) - Ontology property which this slot is a subproperty of
 * [subsets](subsets.md) - list of subsets referenced in this model
 * [symmetric](symmetric.md) - True means that any instance of  d s r implies that there is also an instance of r s d
 * [title](title.md) - the official title of the schema
 * [todos](todos.md) - Outstanding issue that needs resolution
 * [uri](type_uri.md) - The uri that defines the possible values for the type definition
 * [typeof](typeof.md) - Names a parent type
 * [types](types.md) - data types used in the model
 * [union_of](union_of.md) - indicates that the domain class consists exactly of the members of the classes in the range
 * [value](value.md) - example value
 * [description](value_description.md) - description of what the value is doing
 * [values_from](values_from.md) - the identifier of a "value set" -- a set of identifiers that form the possible values for the range of a slot
 * [version](version.md) - particular version of schema
### Types

#### Built in

 * **Bool**
 * **NCName**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**
#### Defined

 * [Boolean](Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Double](Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](Integer.md)  (**int**)  - An integer
 * [Ncname](Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [String](String.md)  (**str**)  - A character string
 * [Time](Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE