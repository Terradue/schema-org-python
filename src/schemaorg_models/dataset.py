from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .data_download import DataDownload
    from .property import Property
    from .statistical_variable import StatisticalVariable
    from .defined_term import DefinedTerm
    from .measurement_method_enum import MeasurementMethodEnum
    from .property_value import PropertyValue
    from .data_catalog import DataCatalog

class Dataset(CreativeWork):
    '''
    A body of structured information describing some topic(s) of interest.

    Attributes:
        issn: The International Standard Serial Number (ISSN) that identifies this serial publication. You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L) for, this serial publication.
        variableMeasured: The variableMeasured property can indicate (repeated as necessary) the  variables that are measured in some dataset, either described as text or as pairs of identifier and description using PropertyValue, or more explicitly as a [[StatisticalVariable]].
        includedDataCatalog: A data catalog which contains this dataset (this property was previously 'catalog', preferred name is now 'includedInDataCatalog').
        includedInDataCatalog: A data catalog which contains this dataset.
        catalog: A data catalog which contains this dataset.
        variablesMeasured: Originally named [[variablesMeasured]], the [[variableMeasured]] property can indicate (repeated as necessary) the  variables that are measured in some dataset, either described as text or as pairs of identifier and description using PropertyValue.
        distribution: A downloadable form of this dataset, at a specific location, in a specific format. This property can be repeated if different variations are available. There is no expectation that different downloadable distributions must contain exactly equivalent information (see also [DCAT](https://www.w3.org/TR/vocab-dcat-3/#Class:Distribution) on this point). Different distributions might include or exclude different subsets of the entire dataset, for example.
        measurementTechnique: A technique, method or technology used in an [[Observation]], [[StatisticalVariable]] or [[Dataset]] (or [[DataDownload]], [[DataCatalog]]), corresponding to the method used for measuring the corresponding variable(s) (for datasets, described using [[variableMeasured]]; for [[Observation]], a [[StatisticalVariable]]). Often but not necessarily each [[variableMeasured]] will have an explicit representation as (or mapping to) an property such as those defined in Schema.org, or other RDF vocabularies and "knowledge graphs". In that case the subproperty of [[variableMeasured]] called [[measuredProperty]] is applicable.
    
The [[measurementTechnique]] property helps when extra clarification is needed about how a [[measuredProperty]] was measured. This is oriented towards scientific and scholarly dataset publication but may have broader applicability; it is not intended as a full representation of measurement, but can often serve as a high level summary for dataset discovery. 

For example, if [[variableMeasured]] is: molecule concentration, [[measurementTechnique]] could be: "mass spectrometry" or "nmr spectroscopy" or "colorimetry" or "immunofluorescence". If the [[variableMeasured]] is "depression rating", the [[measurementTechnique]] could be "Zung Scale" or "HAM-D" or "Beck Depression Inventory". 

If there are several [[variableMeasured]] properties recorded for some given data object, use a [[PropertyValue]] for each [[variableMeasured]] and attach the corresponding [[measurementTechnique]]. The value can also be from an enumeration, organized as a [[MeasurementMetholdEnumeration]].
        datasetTimeInterval: The range of temporal applicability of a dataset, e.g. for a 2011 census dataset, the year 2011 (in ISO 8601 time interval format).
        measurementMethod: A subproperty of [[measurementTechnique]] that can be used for specifying specific methods, in particular via [[MeasurementMethodEnum]].
    '''
    class_: Literal['https://schema.org/Dataset'] = Field( # type: ignore
        default='https://schema.org/Dataset',
        alias='@type',
        serialization_alias='@type'
    )
    issn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'issn',
            'https://schema.org/issn'
        ),
        serialization_alias='https://schema.org/issn'
    )
    variableMeasured: Optional[Union['Property', List['Property'], 'StatisticalVariable', List['StatisticalVariable'], str, List[str], 'PropertyValue', List['PropertyValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'variableMeasured',
            'https://schema.org/variableMeasured'
        ),
        serialization_alias='https://schema.org/variableMeasured'
    )
    includedDataCatalog: Optional[Union['DataCatalog', List['DataCatalog']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includedDataCatalog',
            'https://schema.org/includedDataCatalog'
        ),
        serialization_alias='https://schema.org/includedDataCatalog'
    )
    includedInDataCatalog: Optional[Union['DataCatalog', List['DataCatalog']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includedInDataCatalog',
            'https://schema.org/includedInDataCatalog'
        ),
        serialization_alias='https://schema.org/includedInDataCatalog'
    )
    catalog: Optional[Union['DataCatalog', List['DataCatalog']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'catalog',
            'https://schema.org/catalog'
        ),
        serialization_alias='https://schema.org/catalog'
    )
    variablesMeasured: Optional[Union[str, List[str], 'PropertyValue', List['PropertyValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'variablesMeasured',
            'https://schema.org/variablesMeasured'
        ),
        serialization_alias='https://schema.org/variablesMeasured'
    )
    distribution: Optional[Union['DataDownload', List['DataDownload']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'distribution',
            'https://schema.org/distribution'
        ),
        serialization_alias='https://schema.org/distribution'
    )
    measurementTechnique: Optional[Union['DefinedTerm', List['DefinedTerm'], 'MeasurementMethodEnum', List['MeasurementMethodEnum'], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementTechnique',
            'https://schema.org/measurementTechnique'
        ),
        serialization_alias='https://schema.org/measurementTechnique'
    )
    datasetTimeInterval: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'datasetTimeInterval',
            'https://schema.org/datasetTimeInterval'
        ),
        serialization_alias='https://schema.org/datasetTimeInterval'
    )
    measurementMethod: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str], 'MeasurementMethodEnum', List['MeasurementMethodEnum'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementMethod',
            'https://schema.org/measurementMethod'
        ),
        serialization_alias='https://schema.org/measurementMethod'
    )
