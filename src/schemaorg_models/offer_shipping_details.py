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
    from .monetary_amount import MonetaryAmount
    from .shipping_service import ShippingService
    from .member_program_tier import MemberProgramTier
    from .mass import Mass
    from .defined_region import DefinedRegion
    from .distance import Distance
    from .shipping_delivery_time import ShippingDeliveryTime
    from .quantitative_value import QuantitativeValue
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
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    shippingLabel: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    hasShippingService: Optional[Union['ShippingService', List['ShippingService']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    shippingDestination: Optional[Union['DefinedRegion', List['DefinedRegion']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    deliveryTime: Optional[Union['ShippingDeliveryTime', List['ShippingDeliveryTime']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    doesNotShip: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    width: Optional[Union['QuantitativeValue', List['QuantitativeValue'], 'Distance', List['Distance']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    validForMemberTier: Optional[Union['MemberProgramTier', List['MemberProgramTier']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    shippingOrigin: Optional[Union['DefinedRegion', List['DefinedRegion']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    height: Optional[Union['Distance', List['Distance'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    transitTimeLabel: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    weight: Optional[Union['QuantitativeValue', List['QuantitativeValue'], 'Mass', List['Mass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    shippingRate: Optional[Union['ShippingRateSettings', List['ShippingRateSettings'], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    shippingSettingsLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
