from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.quantitative_value import QuantitativeValue

class QuantitativeValueDistribution(StructuredValue):
    """
A statistical distribution of values.
    """
    median: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('median', 'https://schema.org/median'),serialization_alias='https://schema.org/median')
    percentile75: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('percentile75', 'https://schema.org/percentile75'),serialization_alias='https://schema.org/percentile75')
    percentile25: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('percentile25', 'https://schema.org/percentile25'),serialization_alias='https://schema.org/percentile25')
    percentile90: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('percentile90', 'https://schema.org/percentile90'),serialization_alias='https://schema.org/percentile90')
    percentile10: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('percentile10', 'https://schema.org/percentile10'),serialization_alias='https://schema.org/percentile10')
    duration: Optional[Union["Duration", List["Duration"], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None,validation_alias=AliasChoices('duration', 'https://schema.org/duration'),serialization_alias='https://schema.org/duration')
