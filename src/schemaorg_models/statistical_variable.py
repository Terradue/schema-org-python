from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.constraint_node import ConstraintNode

from schemaorg_models.property import Property
from schemaorg_models.__class import _Class
from schemaorg_models.defined_term import DefinedTerm
from schemaorg_models.measurement_method_enum import MeasurementMethodEnum
from schemaorg_models.enumeration import Enumeration

class StatisticalVariable(ConstraintNode):
    """
[[StatisticalVariable]] represents any type of statistical metric that can be measured at a place and time. The usage pattern for [[StatisticalVariable]] is typically expressed using [[Observation]] with an explicit [[populationType]], which is a type, typically drawn from Schema.org. Each [[StatisticalVariable]] is marked as a [[ConstraintNode]], meaning that some properties (those listed using [[constraintProperty]]) serve in this setting solely to define the statistical variable rather than literally describe a specific person, place or thing. For example, a [[StatisticalVariable]] Median_Height_Person_Female representing the median height of women, could be written as follows: the population type is [[Person]]; the measuredProperty [[height]]; the [[statType]] [[median]]; the [[gender]] [[Female]]. It is important to note that there are many kinds of scientific quantitative observation which are not fully, perfectly or unambiguously described following this pattern, or with solely Schema.org terminology. The approach taken here is designed to allow partial, incremental or minimal description of [[StatisticalVariable]]s, and the use of detailed sets of entity and property IDs from external repositories. The [[measurementMethod]], [[unitCode]] and [[unitText]] properties can also be used to clarify the specific nature and notation of an observed measurement. 
    """
    statType: Optional[Union[HttpUrl, List[HttpUrl], Property, List[Property], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('statType', 'https://schema.org/statType'),serialization_alias='https://schema.org/statType')
    @field_serializer('statType')
    def statType2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    measurementDenominator: Optional[Union["StatisticalVariable", List["StatisticalVariable"]]] = Field(default=None,validation_alias=AliasChoices('measurementDenominator', 'https://schema.org/measurementDenominator'),serialization_alias='https://schema.org/measurementDenominator')
    populationType: Optional[Union[_Class, List[_Class]]] = Field(default=None,validation_alias=AliasChoices('populationType', 'https://schema.org/populationType'),serialization_alias='https://schema.org/populationType')
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str], MeasurementMethodEnum, List[MeasurementMethodEnum], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('measurementMethod', 'https://schema.org/measurementMethod'),serialization_alias='https://schema.org/measurementMethod')
    @field_serializer('measurementMethod')
    def measurementMethod2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    measuredProperty: Optional[Union[Property, List[Property]]] = Field(default=None,validation_alias=AliasChoices('measuredProperty', 'https://schema.org/measuredProperty'),serialization_alias='https://schema.org/measuredProperty')
    measurementQualifier: Optional[Union[Enumeration, List[Enumeration]]] = Field(default=None,validation_alias=AliasChoices('measurementQualifier', 'https://schema.org/measurementQualifier'),serialization_alias='https://schema.org/measurementQualifier')
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm], MeasurementMethodEnum, List[MeasurementMethodEnum], str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('measurementTechnique', 'https://schema.org/measurementTechnique'),serialization_alias='https://schema.org/measurementTechnique')
    @field_serializer('measurementTechnique')
    def measurementTechnique2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

