from typing import Union, List, Optional
from pydantic import AliasChoices, Field, HttpUrl
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.qualitative_value import QualitativeValue

class EngineSpecification(StructuredValue):
    """
Information about the engine of the vehicle. A vehicle can have multiple engines represented by multiple engine specification entities.
    """
    fuelType: Optional[Union[str, List[str], QualitativeValue, List[QualitativeValue], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('fuelType', 'https://schema.org/fuelType'),serialization_alias='https://schema.org/fuelType')
    engineType: Optional[Union[HttpUrl, List[HttpUrl], str, List[str], QualitativeValue, List[QualitativeValue]]] = Field(default=None,validation_alias=AliasChoices('engineType', 'https://schema.org/engineType'),serialization_alias='https://schema.org/engineType')
    engineDisplacement: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('engineDisplacement', 'https://schema.org/engineDisplacement'),serialization_alias='https://schema.org/engineDisplacement')
    enginePower: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('enginePower', 'https://schema.org/enginePower'),serialization_alias='https://schema.org/enginePower')
    torque: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('torque', 'https://schema.org/torque'),serialization_alias='https://schema.org/torque')
