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
    from .opening_hours_specification import OpeningHoursSpecification
    from .quantitative_value import QuantitativeValue
    from .service_period import ServicePeriod
    from .shipping_rate_settings import ShippingRateSettings
    from .mass import Mass
    from .distance import Distance
    from .monetary_amount import MonetaryAmount
    from .defined_region import DefinedRegion

class ShippingConditions(StructuredValue):
    '''
    ShippingConditions represent a set of constraints and information about the conditions of shipping a product. Such conditions may apply to only a subset of the products being shipped, depending on aspects of the product like weight, size, price, destination, and others. All the specified conditions must be met for this ShippingConditions to apply.

    Attributes:
        weight: The weight of the product or person.
        shippingOrigin: Indicates the origin of a shipment, i.e. where it should be coming from.
        shippingDestination: indicates (possibly multiple) shipping destinations. These can be defined in several ways, e.g. postalCode ranges.
        seasonalOverride: Limited period during which these shipping conditions apply.
        shippingRate: The shipping rate is the cost of shipping to the specified destination. Typically, the maxValue and currency values (of the [[MonetaryAmount]]) are most appropriate.
        depth: The depth of the item.
        doesNotShip: Indicates when shipping to a particular [[shippingDestination]] is not available.
        width: The width of the item.
        numItems: Limits the number of items being shipped for which these conditions apply.
        orderValue: Minimum and maximum order value for which these shipping conditions are valid.
        transitTime: The typical delay the order has been sent for delivery and the goods reach the final customer.

  In the context of [[ShippingDeliveryTime]], use the [[QuantitativeValue]]. Typical properties: minValue, maxValue, unitCode (d for DAY).

  In the context of [[ShippingConditions]], use the [[ServicePeriod]]. It has a duration (as a [[QuantitativeValue]]) and also business days and a cut-off time.

        height: The height of the item.
    '''
    class_: Literal['https://schema.org/ShippingConditions'] = Field( # type: ignore
        default='https://schema.org/ShippingConditions',
        alias='@type',
        serialization_alias='@type'
    )
    weight: Optional[Union['QuantitativeValue', List['QuantitativeValue'], 'Mass', List['Mass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'weight',
            'https://schema.org/weight'
        ),
        serialization_alias='https://schema.org/weight'
    )
    shippingOrigin: Optional[Union['DefinedRegion', List['DefinedRegion']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingOrigin',
            'https://schema.org/shippingOrigin'
        ),
        serialization_alias='https://schema.org/shippingOrigin'
    )
    shippingDestination: Optional[Union['DefinedRegion', List['DefinedRegion']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingDestination',
            'https://schema.org/shippingDestination'
        ),
        serialization_alias='https://schema.org/shippingDestination'
    )
    seasonalOverride: Optional[Union['OpeningHoursSpecification', List['OpeningHoursSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seasonalOverride',
            'https://schema.org/seasonalOverride'
        ),
        serialization_alias='https://schema.org/seasonalOverride'
    )
    shippingRate: Optional[Union['ShippingRateSettings', List['ShippingRateSettings'], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingRate',
            'https://schema.org/shippingRate'
        ),
        serialization_alias='https://schema.org/shippingRate'
    )
    depth: Optional[Union['Distance', List['Distance'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'depth',
            'https://schema.org/depth'
        ),
        serialization_alias='https://schema.org/depth'
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
    numItems: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numItems',
            'https://schema.org/numItems'
        ),
        serialization_alias='https://schema.org/numItems'
    )
    orderValue: Optional[Union['MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'orderValue',
            'https://schema.org/orderValue'
        ),
        serialization_alias='https://schema.org/orderValue'
    )
    transitTime: Optional[Union['ServicePeriod', List['ServicePeriod'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'transitTime',
            'https://schema.org/transitTime'
        ),
        serialization_alias='https://schema.org/transitTime'
    )
    height: Optional[Union['Distance', List['Distance'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'height',
            'https://schema.org/height'
        ),
        serialization_alias='https://schema.org/height'
    )
