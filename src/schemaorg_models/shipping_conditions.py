from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.quantitative_value import QuantitativeValue
from schemaorg_models.defined_region import DefinedRegion
from schemaorg_models.shipping_rate_settings import ShippingRateSettings
from schemaorg_models.monetary_amount import MonetaryAmount
from schemaorg_models.service_period import ServicePeriod

class ShippingConditions(StructuredValue):
    """
The conditions (constraints, price) applicable to the [[ShippingService]].
    """
    type_: Literal['https://schema.org/ShippingConditions'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ShippingConditions'),serialization_alias='class') # type: ignore
    weight: Optional[Union[QuantitativeValue, List[QuantitativeValue], "Mass", List["Mass"]]] = Field(default=None,validation_alias=AliasChoices('weight', 'https://schema.org/weight'),serialization_alias='https://schema.org/weight')
    shippingOrigin: Optional[Union[DefinedRegion, List[DefinedRegion]]] = Field(default=None,validation_alias=AliasChoices('shippingOrigin', 'https://schema.org/shippingOrigin'),serialization_alias='https://schema.org/shippingOrigin')
    shippingDestination: Optional[Union[DefinedRegion, List[DefinedRegion]]] = Field(default=None,validation_alias=AliasChoices('shippingDestination', 'https://schema.org/shippingDestination'),serialization_alias='https://schema.org/shippingDestination')
    seasonalOverride: Optional[Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]] = Field(default=None,validation_alias=AliasChoices('seasonalOverride', 'https://schema.org/seasonalOverride'),serialization_alias='https://schema.org/seasonalOverride')
    shippingRate: Optional[Union[ShippingRateSettings, List[ShippingRateSettings], MonetaryAmount, List[MonetaryAmount]]] = Field(default=None,validation_alias=AliasChoices('shippingRate', 'https://schema.org/shippingRate'),serialization_alias='https://schema.org/shippingRate')
    depth: Optional[Union["Distance", List["Distance"], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None,validation_alias=AliasChoices('depth', 'https://schema.org/depth'),serialization_alias='https://schema.org/depth')
    doesNotShip: Optional[Union[bool, List[bool]]] = Field(default=None,validation_alias=AliasChoices('doesNotShip', 'https://schema.org/doesNotShip'),serialization_alias='https://schema.org/doesNotShip')
    width: Optional[Union[QuantitativeValue, List[QuantitativeValue], "Distance", List["Distance"]]] = Field(default=None,validation_alias=AliasChoices('width', 'https://schema.org/width'),serialization_alias='https://schema.org/width')
    numItems: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(default=None,validation_alias=AliasChoices('numItems', 'https://schema.org/numItems'),serialization_alias='https://schema.org/numItems')
    orderValue: Optional[Union[MonetaryAmount, List[MonetaryAmount]]] = Field(default=None,validation_alias=AliasChoices('orderValue', 'https://schema.org/orderValue'),serialization_alias='https://schema.org/orderValue')
    transitTime: Optional[Union[ServicePeriod, List[ServicePeriod], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None,validation_alias=AliasChoices('transitTime', 'https://schema.org/transitTime'),serialization_alias='https://schema.org/transitTime')
    height: Optional[Union["Distance", List["Distance"], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None,validation_alias=AliasChoices('height', 'https://schema.org/height'),serialization_alias='https://schema.org/height')
