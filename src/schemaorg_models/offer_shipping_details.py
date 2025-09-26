from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.quantitative_value import QuantitativeValue
from schemaorg_models.shipping_service import ShippingService
from schemaorg_models.defined_region import DefinedRegion
from schemaorg_models.shipping_delivery_time import ShippingDeliveryTime
from schemaorg_models.member_program_tier import MemberProgramTier
from schemaorg_models.shipping_rate_settings import ShippingRateSettings
from schemaorg_models.monetary_amount import MonetaryAmount

class OfferShippingDetails(StructuredValue):
    """
OfferShippingDetails represents information about shipping destinations.

Multiple of these entities can be used to represent different shipping rates for different destinations:

One entity for Alaska/Hawaii. A different one for continental US. A different one for all France.

Multiple of these entities can be used to represent different shipping costs and delivery times.

Two entities that are identical but differ in rate and time:

E.g. Cheaper and slower: $5 in 5-7 days
or Fast and expensive: $15 in 1-2 days.
    """
    depth: Optional[Union["Distance", List["Distance"], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None,validation_alias=AliasChoices('depth', 'https://schema.org/depth'),serialization_alias='https://schema.org/depth')
    shippingLabel: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('shippingLabel', 'https://schema.org/shippingLabel'),serialization_alias='https://schema.org/shippingLabel')
    hasShippingService: Optional[Union[ShippingService, List[ShippingService]]] = Field(default=None,validation_alias=AliasChoices('hasShippingService', 'https://schema.org/hasShippingService'),serialization_alias='https://schema.org/hasShippingService')
    shippingDestination: Optional[Union[DefinedRegion, List[DefinedRegion]]] = Field(default=None,validation_alias=AliasChoices('shippingDestination', 'https://schema.org/shippingDestination'),serialization_alias='https://schema.org/shippingDestination')
    deliveryTime: Optional[Union[ShippingDeliveryTime, List[ShippingDeliveryTime]]] = Field(default=None,validation_alias=AliasChoices('deliveryTime', 'https://schema.org/deliveryTime'),serialization_alias='https://schema.org/deliveryTime')
    doesNotShip: Optional[Union[bool, List[bool]]] = Field(default=None,validation_alias=AliasChoices('doesNotShip', 'https://schema.org/doesNotShip'),serialization_alias='https://schema.org/doesNotShip')
    width: Optional[Union[QuantitativeValue, List[QuantitativeValue], "Distance", List["Distance"]]] = Field(default=None,validation_alias=AliasChoices('width', 'https://schema.org/width'),serialization_alias='https://schema.org/width')
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = Field(default=None,validation_alias=AliasChoices('validForMemberTier', 'https://schema.org/validForMemberTier'),serialization_alias='https://schema.org/validForMemberTier')
    shippingOrigin: Optional[Union[DefinedRegion, List[DefinedRegion]]] = Field(default=None,validation_alias=AliasChoices('shippingOrigin', 'https://schema.org/shippingOrigin'),serialization_alias='https://schema.org/shippingOrigin')
    height: Optional[Union["Distance", List["Distance"], QuantitativeValue, List[QuantitativeValue]]] = Field(default=None,validation_alias=AliasChoices('height', 'https://schema.org/height'),serialization_alias='https://schema.org/height')
    transitTimeLabel: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('transitTimeLabel', 'https://schema.org/transitTimeLabel'),serialization_alias='https://schema.org/transitTimeLabel')
    weight: Optional[Union[QuantitativeValue, List[QuantitativeValue], "Mass", List["Mass"]]] = Field(default=None,validation_alias=AliasChoices('weight', 'https://schema.org/weight'),serialization_alias='https://schema.org/weight')
    shippingRate: Optional[Union[ShippingRateSettings, List[ShippingRateSettings], MonetaryAmount, List[MonetaryAmount]]] = Field(default=None,validation_alias=AliasChoices('shippingRate', 'https://schema.org/shippingRate'),serialization_alias='https://schema.org/shippingRate')
    shippingSettingsLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('shippingSettingsLink', 'https://schema.org/shippingSettingsLink'),serialization_alias='https://schema.org/shippingSettingsLink')
    @field_serializer('shippingSettingsLink')
    def shippingSettingsLink2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

