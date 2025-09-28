from __future__ import annotations
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
from .constraint_node import ConstraintNode
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .enumeration import Enumeration
    from .measurement_method_enum import MeasurementMethodEnum
    from .__class import _Class
    from .defined_term import DefinedTerm
    from .property import Property

class StatisticalVariable(ConstraintNode):
    """
[[StatisticalVariable]] represents any type of statistical metric that can be measured at a place and time. The usage pattern for [[StatisticalVariable]] is typically expressed using [[Observation]] with an explicit [[populationType]], which is a type, typically drawn from Schema.org. Each [[StatisticalVariable]] is marked as a [[ConstraintNode]], meaning that some properties (those listed using [[constraintProperty]]) serve in this setting solely to define the statistical variable rather than literally describe a specific person, place or thing. For example, a [[StatisticalVariable]] Median_Height_Person_Female representing the median height of women, could be written as follows: the population type is [[Person]]; the measuredProperty [[height]]; the [[statType]] [[median]]; the [[gender]] [[Female]]. It is important to note that there are many kinds of scientific quantitative observation which are not fully, perfectly or unambiguously described following this pattern, or with solely Schema.org terminology. The approach taken here is designed to allow partial, incremental or minimal description of [[StatisticalVariable]]s, and the use of detailed sets of entity and property IDs from external repositories. The [[measurementMethod]], [[unitCode]] and [[unitText]] properties can also be used to clarify the specific nature and notation of an observed measurement. 
    """
    class_: Literal['https://schema.org/StatisticalVariable'] = Field( # type: ignore
        default='https://schema.org/StatisticalVariable',
        alias='@type',
        serialization_alias='@type'
    )
    statType: Optional[Union[HttpUrl, List[HttpUrl], "Property", List["Property"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'statType',
            'https://schema.org/statType'
        ),
        serialization_alias='https://schema.org/statType'
    )
    measurementDenominator: Optional[Union["StatisticalVariable", List["StatisticalVariable"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementDenominator',
            'https://schema.org/measurementDenominator'
        ),
        serialization_alias='https://schema.org/measurementDenominator'
    )
    populationType: Optional[Union["_Class", List["_Class"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'populationType',
            'https://schema.org/populationType'
        ),
        serialization_alias='https://schema.org/populationType'
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
    measurementQualifier: Optional[Union["Enumeration", List["Enumeration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementQualifier',
            'https://schema.org/measurementQualifier'
        ),
        serialization_alias='https://schema.org/measurementQualifier'
    )
    measurementTechnique: Optional[Union["DefinedTerm", List["DefinedTerm"], "MeasurementMethodEnum", List["MeasurementMethodEnum"], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementTechnique',
            'https://schema.org/measurementTechnique'
        ),
        serialization_alias='https://schema.org/measurementTechnique'
    )
