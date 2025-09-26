from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.price_specification import PriceSpecification

from schemaorg_models.duration import Duration
from schemaorg_models.quantitative_value import QuantitativeValue
from schemaorg_models.price_component_type_enumeration import PriceComponentTypeEnumeration
from schemaorg_models.price_type_enumeration import PriceTypeEnumeration

class UnitPriceSpecification(PriceSpecification):
    """
The price asked for a given offer by the respective organization or person.
    """
    unitText: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('unitText', 'https://schema.org/unitText'),serialization_alias='https://schema.org/unitText')
    billingDuration: Optional[Union[Duration, List[Duration], float, List[float], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None,validation_alias=AliasChoices('billingDuration', 'https://schema.org/billingDuration'),serialization_alias='https://schema.org/billingDuration')
    unitCode: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('unitCode', 'https://schema.org/unitCode'),serialization_alias='https://schema.org/unitCode')
    @field_serializer('unitCode')
    def unitCode2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    referenceQuantity: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(default=None,validation_alias=AliasChoices('referenceQuantity', 'https://schema.org/referenceQuantity'),serialization_alias='https://schema.org/referenceQuantity')
    priceComponentType: Optional[Union[PriceComponentTypeEnumeration, List[PriceComponentTypeEnumeration]]] = Field(default=None,validation_alias=AliasChoices('priceComponentType', 'https://schema.org/priceComponentType'),serialization_alias='https://schema.org/priceComponentType')
    billingIncrement: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('billingIncrement', 'https://schema.org/billingIncrement'),serialization_alias='https://schema.org/billingIncrement')
    priceType: Optional[Union[str, List[str], PriceTypeEnumeration, List[PriceTypeEnumeration]]] = Field(default=None,validation_alias=AliasChoices('priceType', 'https://schema.org/priceType'),serialization_alias='https://schema.org/priceType')
    billingStart: Optional[Union[float, List[float]]] = Field(default=None,validation_alias=AliasChoices('billingStart', 'https://schema.org/billingStart'),serialization_alias='https://schema.org/billingStart')
