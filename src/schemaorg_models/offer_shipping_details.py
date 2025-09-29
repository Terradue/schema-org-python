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
from .structured_value import StructuredValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .defined_region import DefinedRegion
    from .monetary_amount import MonetaryAmount
    from .shipping_service import ShippingService
    from .quantitative_value import QuantitativeValue
    from .mass import Mass
    from .member_program_tier import MemberProgramTier
    from .shipping_delivery_time import ShippingDeliveryTime
    from .distance import Distance
    from .shipping_rate_settings import ShippingRateSettings

class OfferShippingDetails(StructuredValue):
    '''
    OfferShippingDetails represents information about shipping destinations.

Multiple of these entities can be used to represent different shipping rates for different destinations:

One entity for Alaska/Hawaii. A different one for continental US. A different one for all France.

Multiple of these entities can be used to represent different shipping costs and delivery times.

Two entities that are identical but differ in rate and time:

E.g. Cheaper and slower: $5 in 5-7 days
or Fast and expensive: $15 in 1-2 days.

    Attributes:
        depth: The depth of the item.
        shippingLabel: Label to match an [[OfferShippingDetails]] with a [[ShippingRateSettings]] (within the context of a [[shippingSettingsLink]] cross-reference).
        hasShippingService: Specification of a shipping service offered by the organization.
        shippingDestination: indicates (possibly multiple) shipping destinations. These can be defined in several ways, e.g. postalCode ranges.
        deliveryTime: The total delay between the receipt of the order and the goods reaching the final customer.
        doesNotShip: Indicates when shipping to a particular [[shippingDestination]] is not available.
        width: The width of the item.
        validForMemberTier: The membership program tier an Offer (or a PriceSpecification, OfferShippingDetails, or MerchantReturnPolicy under an Offer) is valid for.
        shippingOrigin: Indicates the origin of a shipment, i.e. where it should be coming from.
        height: The height of the item.
        transitTimeLabel: Label to match an [[OfferShippingDetails]] with a [[DeliveryTimeSettings]] (within the context of a [[shippingSettingsLink]] cross-reference).
        weight: The weight of the product or person.
        shippingRate: The shipping rate is the cost of shipping to the specified destination. Typically, the maxValue and currency values (of the [[MonetaryAmount]]) are most appropriate.
        shippingSettingsLink: Link to a page containing [[ShippingRateSettings]] and [[DeliveryTimeSettings]] details.
    '''
    class_: Literal['https://schema.org/OfferShippingDetails'] = Field( # type: ignore
        default='https://schema.org/OfferShippingDetails',
        alias='@type',
        serialization_alias='@type'
    )
    depth: Optional[Union['Distance', List['Distance'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'depth',
            'https://schema.org/depth'
        ),
        serialization_alias='https://schema.org/depth'
    )
    shippingLabel: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingLabel',
            'https://schema.org/shippingLabel'
        ),
        serialization_alias='https://schema.org/shippingLabel'
    )
    hasShippingService: Optional[Union['ShippingService', List['ShippingService']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasShippingService',
            'https://schema.org/hasShippingService'
        ),
        serialization_alias='https://schema.org/hasShippingService'
    )
    shippingDestination: Optional[Union['DefinedRegion', List['DefinedRegion']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingDestination',
            'https://schema.org/shippingDestination'
        ),
        serialization_alias='https://schema.org/shippingDestination'
    )
    deliveryTime: Optional[Union['ShippingDeliveryTime', List['ShippingDeliveryTime']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deliveryTime',
            'https://schema.org/deliveryTime'
        ),
        serialization_alias='https://schema.org/deliveryTime'
    )
    doesNotShip: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'doesNotShip',
            'https://schema.org/doesNotShip'
        ),
        serialization_alias='https://schema.org/doesNotShip'
    )
    width: Optional[Union['QuantitativeValue', List['QuantitativeValue'], 'Distance', List['Distance']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'width',
            'https://schema.org/width'
        ),
        serialization_alias='https://schema.org/width'
    )
    validForMemberTier: Optional[Union['MemberProgramTier', List['MemberProgramTier']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validForMemberTier',
            'https://schema.org/validForMemberTier'
        ),
        serialization_alias='https://schema.org/validForMemberTier'
    )
    shippingOrigin: Optional[Union['DefinedRegion', List['DefinedRegion']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingOrigin',
            'https://schema.org/shippingOrigin'
        ),
        serialization_alias='https://schema.org/shippingOrigin'
    )
    height: Optional[Union['Distance', List['Distance'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'height',
            'https://schema.org/height'
        ),
        serialization_alias='https://schema.org/height'
    )
    transitTimeLabel: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'transitTimeLabel',
            'https://schema.org/transitTimeLabel'
        ),
        serialization_alias='https://schema.org/transitTimeLabel'
    )
    weight: Optional[Union['QuantitativeValue', List['QuantitativeValue'], 'Mass', List['Mass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'weight',
            'https://schema.org/weight'
        ),
        serialization_alias='https://schema.org/weight'
    )
    shippingRate: Optional[Union['ShippingRateSettings', List['ShippingRateSettings'], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingRate',
            'https://schema.org/shippingRate'
        ),
        serialization_alias='https://schema.org/shippingRate'
    )
    shippingSettingsLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingSettingsLink',
            'https://schema.org/shippingSettingsLink'
        ),
        serialization_alias='https://schema.org/shippingSettingsLink'
    )
