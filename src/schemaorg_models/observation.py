from __future__ import annotations
from datetime import (
    datetime
)
from pydantic import (
    AliasChoices,
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
    from .measurement_method_enum import MeasurementMethodEnum
    from .place import Place
    from .enumeration import Enumeration
    from .property import Property
    from .quantitative_value import QuantitativeValue
    from .property_value import PropertyValue
    from .thing import Thing
    from .defined_term import DefinedTerm
    from .statistical_variable import StatisticalVariable

class Observation(Intangible):
    """
Instances of the class [[Observation]] are used to specify observations about an entity at a particular time. The principal properties of an [[Observation]] are [[observationAbout]], [[measuredProperty]], [[statType]], [[value] and [[observationDate]]  and [[measuredProperty]]. Some but not all Observations represent a [[QuantitativeValue]]. Quantitative observations can be about a [[StatisticalVariable]], which is an abstract specification about which we can make observations that are grounded at a particular location and time.

Observations can also encode a subset of simple RDF-like statements (its observationAbout, a StatisticalVariable, defining the measuredPoperty; its observationAbout property indicating the entity the statement is about, and [[value]] )

In the context of a quantitative knowledge graph, typical properties could include [[measuredProperty]], [[observationAbout]], [[observationDate]], [[value]], [[unitCode]], [[unitText]], [[measurementMethod]].
    
    """
    class_: Literal['https://schema.org/Observation'] = Field( # type: ignore
        default='https://schema.org/Observation',
        alias='@type',
        serialization_alias='@type'
    )
    measurementTechnique: Optional[Union["DefinedTerm", List["DefinedTerm"], "MeasurementMethodEnum", List["MeasurementMethodEnum"], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementTechnique',
            'https://schema.org/measurementTechnique'
        ),
        serialization_alias='https://schema.org/measurementTechnique'
    )
    marginOfError: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
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
    measurementDenominator: Optional[Union["StatisticalVariable", List["StatisticalVariable"]]] = Field(
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
    measurementMethod: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str], "MeasurementMethodEnum", List["MeasurementMethodEnum"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementMethod',
            'https://schema.org/measurementMethod'
        ),
        serialization_alias='https://schema.org/measurementMethod'
    )
    measuredProperty: Optional[Union["Property", List["Property"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measuredProperty',
            'https://schema.org/measuredProperty'
        ),
        serialization_alias='https://schema.org/measuredProperty'
    )
    observationAbout: Optional[Union["Thing", List["Thing"], "Place", List["Place"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'observationAbout',
            'https://schema.org/observationAbout'
        ),
        serialization_alias='https://schema.org/observationAbout'
    )
    variableMeasured: Optional[Union["Property", List["Property"], "StatisticalVariable", List["StatisticalVariable"], str, List[str], "PropertyValue", List["PropertyValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'variableMeasured',
            'https://schema.org/variableMeasured'
        ),
        serialization_alias='https://schema.org/variableMeasured'
    )
    measurementQualifier: Optional[Union["Enumeration", List["Enumeration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementQualifier',
            'https://schema.org/measurementQualifier'
        ),
        serialization_alias='https://schema.org/measurementQualifier'
    )
