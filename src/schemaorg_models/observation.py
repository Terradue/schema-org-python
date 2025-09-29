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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .place import Place
    from .property_value import PropertyValue
    from .measurement_method_enum import MeasurementMethodEnum
    from .statistical_variable import StatisticalVariable
    from .property import Property
    from .thing import Thing
    from .defined_term import DefinedTerm
    from .quantitative_value import QuantitativeValue
    from .enumeration import Enumeration

class Observation(Intangible):
    '''
    Instances of the class [[Observation]] are used to specify observations about an entity at a particular time. The principal properties of an [[Observation]] are [[observationAbout]], [[measuredProperty]], [[statType]], [[value] and [[observationDate]]  and [[measuredProperty]]. Some but not all Observations represent a [[QuantitativeValue]]. Quantitative observations can be about a [[StatisticalVariable]], which is an abstract specification about which we can make observations that are grounded at a particular location and time.

Observations can also encode a subset of simple RDF-like statements (its observationAbout, a StatisticalVariable, defining the measuredPoperty; its observationAbout property indicating the entity the statement is about, and [[value]] )

In the context of a quantitative knowledge graph, typical properties could include [[measuredProperty]], [[observationAbout]], [[observationDate]], [[value]], [[unitCode]], [[unitText]], [[measurementMethod]].
    

    Attributes:
        measurementTechnique: A technique, method or technology used in an [[Observation]], [[StatisticalVariable]] or [[Dataset]] (or [[DataDownload]], [[DataCatalog]]), corresponding to the method used for measuring the corresponding variable(s) (for datasets, described using [[variableMeasured]]; for [[Observation]], a [[StatisticalVariable]]). Often but not necessarily each [[variableMeasured]] will have an explicit representation as (or mapping to) an property such as those defined in Schema.org, or other RDF vocabularies and "knowledge graphs". In that case the subproperty of [[variableMeasured]] called [[measuredProperty]] is applicable.
    
The [[measurementTechnique]] property helps when extra clarification is needed about how a [[measuredProperty]] was measured. This is oriented towards scientific and scholarly dataset publication but may have broader applicability; it is not intended as a full representation of measurement, but can often serve as a high level summary for dataset discovery. 

For example, if [[variableMeasured]] is: molecule concentration, [[measurementTechnique]] could be: "mass spectrometry" or "nmr spectroscopy" or "colorimetry" or "immunofluorescence". If the [[variableMeasured]] is "depression rating", the [[measurementTechnique]] could be "Zung Scale" or "HAM-D" or "Beck Depression Inventory". 

If there are several [[variableMeasured]] properties recorded for some given data object, use a [[PropertyValue]] for each [[variableMeasured]] and attach the corresponding [[measurementTechnique]]. The value can also be from an enumeration, organized as a [[MeasurementMetholdEnumeration]].
        marginOfError: A [[marginOfError]] for an [[Observation]].
        observationPeriod: The length of time an Observation took place over. The format follows `P[0-9]*[Y|M|D|h|m|s]`. For example, P1Y is Period 1 Year, P3M is Period 3 Months, P3h is Period 3 hours.
        measurementDenominator: Identifies the denominator variable when an observation represents a ratio or percentage.
        observationDate: The observationDate of an [[Observation]].
        measurementMethod: A subproperty of [[measurementTechnique]] that can be used for specifying specific methods, in particular via [[MeasurementMethodEnum]].
        measuredProperty: The measuredProperty of an [[Observation]], typically via its [[StatisticalVariable]]. There are various kinds of applicable [[Property]]: a schema.org property, a property from other RDF-compatible systems, e.g. W3C RDF Data Cube, Data Commons, Wikidata, or schema.org extensions such as [GS1's](https://www.gs1.org/voc/?show=properties).
        observationAbout: The [[observationAbout]] property identifies an entity, often a [[Place]], associated with an [[Observation]].
        variableMeasured: The variableMeasured property can indicate (repeated as necessary) the  variables that are measured in some dataset, either described as text or as pairs of identifier and description using PropertyValue, or more explicitly as a [[StatisticalVariable]].
        measurementQualifier: Provides additional qualification to an observation. For example, a GDP observation measures the Nominal value.
    '''
    class_: Literal['https://schema.org/Observation'] = Field( # type: ignore
        default='https://schema.org/Observation',
        alias='@type',
        serialization_alias='@type'
    )
    measurementTechnique: Optional[Union['DefinedTerm', List['DefinedTerm'], 'MeasurementMethodEnum', List['MeasurementMethodEnum'], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementTechnique',
            'https://schema.org/measurementTechnique'
        ),
        serialization_alias='https://schema.org/measurementTechnique'
    )
    marginOfError: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'marginOfError',
            'https://schema.org/marginOfError'
        ),
        serialization_alias='https://schema.org/marginOfError'
    )
    observationPeriod: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'observationPeriod',
            'https://schema.org/observationPeriod'
        ),
        serialization_alias='https://schema.org/observationPeriod'
    )
    measurementDenominator: Optional[Union['StatisticalVariable', List['StatisticalVariable']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementDenominator',
            'https://schema.org/measurementDenominator'
        ),
        serialization_alias='https://schema.org/measurementDenominator'
    )
    observationDate: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'observationDate',
            'https://schema.org/observationDate'
        ),
        serialization_alias='https://schema.org/observationDate'
    )
    measurementMethod: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str], 'MeasurementMethodEnum', List['MeasurementMethodEnum'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementMethod',
            'https://schema.org/measurementMethod'
        ),
        serialization_alias='https://schema.org/measurementMethod'
    )
    measuredProperty: Optional[Union['Property', List['Property']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measuredProperty',
            'https://schema.org/measuredProperty'
        ),
        serialization_alias='https://schema.org/measuredProperty'
    )
    observationAbout: Optional[Union['Thing', List['Thing'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'observationAbout',
            'https://schema.org/observationAbout'
        ),
        serialization_alias='https://schema.org/observationAbout'
    )
    variableMeasured: Optional[Union['Property', List['Property'], 'StatisticalVariable', List['StatisticalVariable'], str, List[str], 'PropertyValue', List['PropertyValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'variableMeasured',
            'https://schema.org/variableMeasured'
        ),
        serialization_alias='https://schema.org/variableMeasured'
    )
    measurementQualifier: Optional[Union['Enumeration', List['Enumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementQualifier',
            'https://schema.org/measurementQualifier'
        ),
        serialization_alias='https://schema.org/measurementQualifier'
    )
