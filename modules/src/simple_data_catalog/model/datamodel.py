from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'sdc',
     'default_range': 'Any',
     'id': 'https://w3id.org/linkml/examples/personinfo',
     'imports': ['linkml:types'],
     'name': 'data_catalog_model',
     'prefixes': {'dcat': {'prefix_prefix': 'dcat',
                           'prefix_reference': 'http://www.w3.org/ns/dcat#'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'dqv': {'prefix_prefix': 'dqv',
                          'prefix_reference': 'http://www.w3.org/ns/dqv#'},
                  'ex': {'prefix_prefix': 'ex',
                         'prefix_reference': 'www.example.com/'},
                  'foaf': {'prefix_prefix': 'foaf',
                           'prefix_reference': 'http://xmlns.com/foaf/0.1/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'odrl': {'prefix_prefix': 'odrl',
                           'prefix_reference': 'http://www.w3.org/ns/odrl/2/'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'sdc': {'prefix_prefix': 'sdc',
                          'prefix_reference': 'https://w3id.org/simpledatacatalog/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'time': {'prefix_prefix': 'time',
                           'prefix_reference': 'http://www.w3.org/2006/time#'},
                  'vcard': {'prefix_prefix': 'vcard',
                            'prefix_reference': 'http://www.w3.org/2006/vcard/ns#'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'source_file': 'src/simple_data_catalog_model/dataset_model.yaml'} )

class Dimension(str, Enum):
    Accuracy = "Accuracy"
    Completeness = "Completeness"
    Consistency = "Consistency"
    Credibility = "Credibility"
    Currentness = "Currentness"
    Accessibility = "Accessibility"
    Compliance = "Compliance"
    Confidentiality = "Confidentiality"
    Efficiency = "Efficiency"
    Precision = "Precision"
    Traceability = "Traceability"
    Understandeability = "Understandeability"
    Availability = "Availability"
    Portability = "Portability"
    Recoverability = "Recoverability"



class URI(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/examples/personinfo'})

    pass


class Resource(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dcat:resource',
         'from_schema': 'https://w3id.org/linkml/examples/personinfo'})

    identifier: str = Field(default=..., description="""An unambiguous reference to the resource within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'domain_of': ['Resource',
                       'Concept',
                       'Distribution',
                       'Metric',
                       'QualityMeasurement'],
         'slot_uri': 'dcterms:identifier'} })
    description: Optional[str] = Field(default=None, description="""Description may include but is not limited to: an abstract, a table of contents, a graphical representation, or a free-text account of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Resource', 'Distribution'],
         'slot_uri': 'dcterms:identifier'} })
    title: Optional[str] = Field(default=None, description="""A name given to the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Resource', 'LiceneseDocument', 'Distribution'],
         'slot_uri': 'dcterms:title'} })
    publisher: Optional[Agent] = Field(default=None, description="""An entity responsible for making the resource available.""", json_schema_extra = { "linkml_meta": {'alias': 'publisher',
         'domain_of': ['Resource'],
         'slot_uri': 'dcterms:publisher'} })
    contactPoint: Optional[Kind] = Field(default=None, description="""Relevant contact information for the cataloged resource. Use of vCard is recommended""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['Resource'],
         'slot_uri': 'vcard:contactPoint'} })
    license: Optional[LiceneseDocument] = Field(default=None, description="""A legal document giving official permission to do something with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource'], 'slot_uri': 'dcterms:license'} })
    status: Optional[str] = Field(default=None, description="""The status of the Asset in the context of a particular workflow process.""", json_schema_extra = { "linkml_meta": {'alias': 'status', 'domain_of': ['Resource'], 'slot_uri': 'time:hasEnd'} })
    theme: Optional[List[str]] = Field(default=None, description="""A main category of the resource. A resource can have multiple themes.""", json_schema_extra = { "linkml_meta": {'alias': 'theme', 'domain_of': ['Resource'], 'slot_uri': 'dcat:theme'} })
    wasDerivedFrom: Optional[str] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""", json_schema_extra = { "linkml_meta": {'alias': 'wasDerivedFrom',
         'domain_of': ['Resource'],
         'slot_uri': 'prov:wasDerivedFrom'} })


class Dataset(Resource):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dcat:Dataset',
         'from_schema': 'https://w3id.org/linkml/examples/personinfo'})

    temporal: Optional[PeriodOfTime] = Field(default=None, description="""Temporal characteristics of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'temporal', 'domain_of': ['Dataset'], 'slot_uri': 'dcat:version'} })
    distribution: Optional[str] = Field(default=None, description="""An available distribution of the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'distribution',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcat:distribution'} })
    inSeries: Optional[str] = Field(default=None, description=""".""", json_schema_extra = { "linkml_meta": {'alias': 'inSeries', 'domain_of': ['Dataset'], 'slot_uri': 'dcat:inSeries'} })
    identifier: str = Field(default=..., description="""An unambiguous reference to the resource within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'domain_of': ['Resource',
                       'Concept',
                       'Distribution',
                       'Metric',
                       'QualityMeasurement'],
         'slot_uri': 'dcterms:identifier'} })
    description: Optional[str] = Field(default=None, description="""Description may include but is not limited to: an abstract, a table of contents, a graphical representation, or a free-text account of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Resource', 'Distribution'],
         'slot_uri': 'dcterms:identifier'} })
    title: Optional[str] = Field(default=None, description="""A name given to the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Resource', 'LiceneseDocument', 'Distribution'],
         'slot_uri': 'dcterms:title'} })
    publisher: Optional[Agent] = Field(default=None, description="""An entity responsible for making the resource available.""", json_schema_extra = { "linkml_meta": {'alias': 'publisher',
         'domain_of': ['Resource'],
         'slot_uri': 'dcterms:publisher'} })
    contactPoint: Optional[Kind] = Field(default=None, description="""Relevant contact information for the cataloged resource. Use of vCard is recommended""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['Resource'],
         'slot_uri': 'vcard:contactPoint'} })
    license: Optional[LiceneseDocument] = Field(default=None, description="""A legal document giving official permission to do something with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource'], 'slot_uri': 'dcterms:license'} })
    status: Optional[str] = Field(default=None, description="""The status of the Asset in the context of a particular workflow process.""", json_schema_extra = { "linkml_meta": {'alias': 'status', 'domain_of': ['Resource'], 'slot_uri': 'time:hasEnd'} })
    theme: Optional[List[str]] = Field(default=None, description="""A main category of the resource. A resource can have multiple themes.""", json_schema_extra = { "linkml_meta": {'alias': 'theme', 'domain_of': ['Resource'], 'slot_uri': 'dcat:theme'} })
    wasDerivedFrom: Optional[str] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""", json_schema_extra = { "linkml_meta": {'alias': 'wasDerivedFrom',
         'domain_of': ['Resource'],
         'slot_uri': 'prov:wasDerivedFrom'} })


class Agent(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'foaf:Agent',
         'from_schema': 'https://w3id.org/linkml/examples/personinfo'})

    name: Optional[str] = Field(default=None, description="""A name for some thing""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Agent'], 'slot_uri': 'foaf:name'} })


class Kind(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'vcard:Kind',
         'from_schema': 'https://w3id.org/linkml/examples/personinfo'})

    hasEmail: Optional[str] = Field(default=None, description="""Relevant contact information for the cataloged resource. Use of vCard is recommended""", json_schema_extra = { "linkml_meta": {'alias': 'hasEmail', 'domain_of': ['Kind'], 'slot_uri': 'vcard:hasEmail'} })


class LiceneseDocument(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dcterms:LicenseDocument',
         'from_schema': 'https://w3id.org/linkml/examples/personinfo'})

    title: Optional[str] = Field(default=None, description="""A name given to the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Resource', 'LiceneseDocument', 'Distribution'],
         'slot_uri': 'dcterms:title'} })


class PeriodOfTime(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dcterms:PeriodOfTime',
         'from_schema': 'https://w3id.org/linkml/examples/personinfo'})

    hasBeginning: Optional[date] = Field(default=None, description="""Temporal characteristics of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'hasBeginning',
         'domain_of': ['PeriodOfTime'],
         'slot_uri': 'time:hasBeginning'} })
    hasEnd: Optional[date] = Field(default=None, description="""Temporal characteristics of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'hasEnd', 'domain_of': ['PeriodOfTime'], 'slot_uri': 'time:hasEnd'} })


class Concept(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'skos:Concept',
         'from_schema': 'https://w3id.org/linkml/examples/personinfo'})

    prefLabel: Optional[str] = Field(default=None, description="""The preferred lexical label for a resource, in a given language.""", json_schema_extra = { "linkml_meta": {'alias': 'prefLabel',
         'domain_of': ['Concept', 'Metric'],
         'slot_uri': 'skos:prefLabel'} })
    identifier: str = Field(default=..., description="""An unambiguous reference to the resource within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'domain_of': ['Resource',
                       'Concept',
                       'Distribution',
                       'Metric',
                       'QualityMeasurement'],
         'slot_uri': 'dcterms:identifier'} })
    definition: Optional[str] = Field(default=None, description="""A statement or formal explanation of the meaning of a concept.""", json_schema_extra = { "linkml_meta": {'alias': 'definition',
         'domain_of': ['Concept', 'Metric'],
         'slot_uri': 'skos:definition'} })
    example: Optional[str] = Field(default=None, description="""An example of the use of a concept.""", json_schema_extra = { "linkml_meta": {'alias': 'example', 'domain_of': ['Concept'], 'slot_uri': 'skos:example'} })
    altLabel: Optional[str] = Field(default=None, description="""An alternative lexical label for a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'altLabel', 'domain_of': ['Concept'], 'slot_uri': 'skos:altLabel'} })


class DatasetSeries(Dataset):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/examples/personinfo'})

    temporal: Optional[PeriodOfTime] = Field(default=None, description="""Temporal characteristics of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'temporal', 'domain_of': ['Dataset'], 'slot_uri': 'dcat:version'} })
    distribution: Optional[str] = Field(default=None, description="""An available distribution of the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'distribution',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcat:distribution'} })
    inSeries: Optional[str] = Field(default=None, description=""".""", json_schema_extra = { "linkml_meta": {'alias': 'inSeries', 'domain_of': ['Dataset'], 'slot_uri': 'dcat:inSeries'} })
    identifier: str = Field(default=..., description="""An unambiguous reference to the resource within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'domain_of': ['Resource',
                       'Concept',
                       'Distribution',
                       'Metric',
                       'QualityMeasurement'],
         'slot_uri': 'dcterms:identifier'} })
    description: Optional[str] = Field(default=None, description="""Description may include but is not limited to: an abstract, a table of contents, a graphical representation, or a free-text account of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Resource', 'Distribution'],
         'slot_uri': 'dcterms:identifier'} })
    title: Optional[str] = Field(default=None, description="""A name given to the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Resource', 'LiceneseDocument', 'Distribution'],
         'slot_uri': 'dcterms:title'} })
    publisher: Optional[Agent] = Field(default=None, description="""An entity responsible for making the resource available.""", json_schema_extra = { "linkml_meta": {'alias': 'publisher',
         'domain_of': ['Resource'],
         'slot_uri': 'dcterms:publisher'} })
    contactPoint: Optional[Kind] = Field(default=None, description="""Relevant contact information for the cataloged resource. Use of vCard is recommended""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['Resource'],
         'slot_uri': 'vcard:contactPoint'} })
    license: Optional[LiceneseDocument] = Field(default=None, description="""A legal document giving official permission to do something with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource'], 'slot_uri': 'dcterms:license'} })
    status: Optional[str] = Field(default=None, description="""The status of the Asset in the context of a particular workflow process.""", json_schema_extra = { "linkml_meta": {'alias': 'status', 'domain_of': ['Resource'], 'slot_uri': 'time:hasEnd'} })
    theme: Optional[List[str]] = Field(default=None, description="""A main category of the resource. A resource can have multiple themes.""", json_schema_extra = { "linkml_meta": {'alias': 'theme', 'domain_of': ['Resource'], 'slot_uri': 'dcat:theme'} })
    wasDerivedFrom: Optional[str] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""", json_schema_extra = { "linkml_meta": {'alias': 'wasDerivedFrom',
         'domain_of': ['Resource'],
         'slot_uri': 'prov:wasDerivedFrom'} })


class DataCatalog(Dataset):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/examples/personinfo'})

    dataset: Optional[List[str]] = Field(default=None, description=""".""", json_schema_extra = { "linkml_meta": {'alias': 'dataset', 'domain_of': ['DataCatalog'], 'slot_uri': 'dcat:dataset'} })
    temporal: Optional[PeriodOfTime] = Field(default=None, description="""Temporal characteristics of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'temporal', 'domain_of': ['Dataset'], 'slot_uri': 'dcat:version'} })
    distribution: Optional[str] = Field(default=None, description="""An available distribution of the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'distribution',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcat:distribution'} })
    inSeries: Optional[str] = Field(default=None, description=""".""", json_schema_extra = { "linkml_meta": {'alias': 'inSeries', 'domain_of': ['Dataset'], 'slot_uri': 'dcat:inSeries'} })
    identifier: str = Field(default=..., description="""An unambiguous reference to the resource within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'domain_of': ['Resource',
                       'Concept',
                       'Distribution',
                       'Metric',
                       'QualityMeasurement'],
         'slot_uri': 'dcterms:identifier'} })
    description: Optional[str] = Field(default=None, description="""Description may include but is not limited to: an abstract, a table of contents, a graphical representation, or a free-text account of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Resource', 'Distribution'],
         'slot_uri': 'dcterms:identifier'} })
    title: Optional[str] = Field(default=None, description="""A name given to the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Resource', 'LiceneseDocument', 'Distribution'],
         'slot_uri': 'dcterms:title'} })
    publisher: Optional[Agent] = Field(default=None, description="""An entity responsible for making the resource available.""", json_schema_extra = { "linkml_meta": {'alias': 'publisher',
         'domain_of': ['Resource'],
         'slot_uri': 'dcterms:publisher'} })
    contactPoint: Optional[Kind] = Field(default=None, description="""Relevant contact information for the cataloged resource. Use of vCard is recommended""", json_schema_extra = { "linkml_meta": {'alias': 'contactPoint',
         'domain_of': ['Resource'],
         'slot_uri': 'vcard:contactPoint'} })
    license: Optional[LiceneseDocument] = Field(default=None, description="""A legal document giving official permission to do something with the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'license', 'domain_of': ['Resource'], 'slot_uri': 'dcterms:license'} })
    status: Optional[str] = Field(default=None, description="""The status of the Asset in the context of a particular workflow process.""", json_schema_extra = { "linkml_meta": {'alias': 'status', 'domain_of': ['Resource'], 'slot_uri': 'time:hasEnd'} })
    theme: Optional[List[str]] = Field(default=None, description="""A main category of the resource. A resource can have multiple themes.""", json_schema_extra = { "linkml_meta": {'alias': 'theme', 'domain_of': ['Resource'], 'slot_uri': 'dcat:theme'} })
    wasDerivedFrom: Optional[str] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""", json_schema_extra = { "linkml_meta": {'alias': 'wasDerivedFrom',
         'domain_of': ['Resource'],
         'slot_uri': 'prov:wasDerivedFrom'} })


class Distribution(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/examples/personinfo'})

    identifier: str = Field(default=..., description="""An unambiguous reference to the resource within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'domain_of': ['Resource',
                       'Concept',
                       'Distribution',
                       'Metric',
                       'QualityMeasurement'],
         'slot_uri': 'dcterms:identifier'} })
    title: Optional[str] = Field(default=None, description="""A name given to the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Resource', 'LiceneseDocument', 'Distribution'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""Description may include but is not limited to: an abstract, a table of contents, a graphical representation, or a free-text account of the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Resource', 'Distribution'],
         'slot_uri': 'dcterms:identifier'} })
    accessURL: Optional[str] = Field(default=None, description="""A URL of the resource that gives access to a distribution of the dataset. E.g., landing page, feed, SPARQL endpoint. """, json_schema_extra = { "linkml_meta": {'alias': 'accessURL',
         'domain_of': ['Distribution'],
         'slot_uri': 'dcat:accessURL'} })
    modified: Optional[date] = Field(default=None, description="""date on which the resource was changed.""", json_schema_extra = { "linkml_meta": {'alias': 'modified', 'domain_of': ['Distribution'], 'slot_uri': 'dcat:theme'} })
    version: Optional[str] = Field(default=None, description="""The version indicator (name or identifier) of a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['Distribution'], 'slot_uri': 'dcat:version'} })


class Metric(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/examples/personinfo'})

    identifier: str = Field(default=..., description="""An unambiguous reference to the resource within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'domain_of': ['Resource',
                       'Concept',
                       'Distribution',
                       'Metric',
                       'QualityMeasurement'],
         'slot_uri': 'dcterms:identifier'} })
    prefLabel: Optional[str] = Field(default=None, description="""The preferred lexical label for a resource, in a given language.""", json_schema_extra = { "linkml_meta": {'alias': 'prefLabel',
         'domain_of': ['Concept', 'Metric'],
         'slot_uri': 'skos:prefLabel'} })
    definition: Optional[str] = Field(default=None, description="""A statement or formal explanation of the meaning of a concept.""", json_schema_extra = { "linkml_meta": {'alias': 'definition',
         'domain_of': ['Concept', 'Metric'],
         'slot_uri': 'skos:definition'} })
    expectedDataType: Optional[Any] = Field(default=None, description="""Represents the expected data type for the metric's observed value (e.g., xsd:boolean, xsd:double etc...) """, json_schema_extra = { "linkml_meta": {'alias': 'expectedDataType',
         'domain_of': ['Metric'],
         'slot_uri': 'dqv:expectedDataType'} })
    inDimension: Optional[Dimension] = Field(default=None, description="""Represents the expected data type for the metric's observed value (e.g., xsd:boolean, xsd:double etc...) """, json_schema_extra = { "linkml_meta": {'alias': 'inDimension', 'domain_of': ['Metric'], 'slot_uri': 'dqv:inDimension'} })


class QualityMeasurement(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/examples/personinfo'})

    identifier: str = Field(default=..., description="""An unambiguous reference to the resource within a given context.""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'domain_of': ['Resource',
                       'Concept',
                       'Distribution',
                       'Metric',
                       'QualityMeasurement'],
         'slot_uri': 'dcterms:identifier'} })
    computedOn: str = Field(default=..., description="""Refers to the resource (e.g., a dataset, a linkset, a graph, a set of triples) on which the quality measurement is performed. In the DQV context, this property is generally expected to be used in statements in which objects are instances of dcat:Dataset or dcat:Distribution. """, json_schema_extra = { "linkml_meta": {'alias': 'computedOn',
         'domain_of': ['QualityMeasurement'],
         'slot_uri': 'dqv:computedOn'} })
    isMeasurementOf: Optional[str] = Field(default=None, description="""Indicates the metric being observed.""", json_schema_extra = { "linkml_meta": {'alias': 'isMeasurementOf',
         'domain_of': ['QualityMeasurement'],
         'slot_uri': 'dqv:isMeasurementOf'} })
    generatedAtTime: Optional[date] = Field(default=None, description="""Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.""", json_schema_extra = { "linkml_meta": {'alias': 'generatedAtTime',
         'domain_of': ['QualityMeasurement'],
         'slot_uri': 'prov:generatedAtTime'} })
    value: Optional[float] = Field(default=None, description="""Refers to values computed by metric.""", json_schema_extra = { "linkml_meta": {'alias': 'value', 'domain_of': ['QualityMeasurement'], 'slot_uri': 'dqv:value'} })


class Container(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/examples/personinfo',
         'tree_root': True})

    datasets: Optional[List[Dataset]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'datasets', 'domain_of': ['Container']} })
    concepts: Optional[List[Concept]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'concepts', 'domain_of': ['Container']} })
    series: Optional[List[DatasetSeries]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'series', 'domain_of': ['Container']} })
    dataCatalog: DataCatalog = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'dataCatalog', 'domain_of': ['Container']} })
    distributions: Optional[List[Distribution]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'distributions', 'domain_of': ['Container']} })
    metrics: Optional[List[Metric]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'metrics', 'domain_of': ['Container']} })
    qualityMeasurements: Optional[List[QualityMeasurement]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'qualityMeasurements', 'domain_of': ['Container']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
URI.model_rebuild()
Resource.model_rebuild()
Dataset.model_rebuild()
Agent.model_rebuild()
Kind.model_rebuild()
LiceneseDocument.model_rebuild()
PeriodOfTime.model_rebuild()
Concept.model_rebuild()
DatasetSeries.model_rebuild()
DataCatalog.model_rebuild()
Distribution.model_rebuild()
Metric.model_rebuild()
QualityMeasurement.model_rebuild()
Container.model_rebuild()

