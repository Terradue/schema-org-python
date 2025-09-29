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
    from .shipping_delivery_time import ShippingDeliveryTime
    from .defined_region import DefinedRegion

class DeliveryTimeSettings(StructuredValue):
    '''
    A DeliveryTimeSettings represents re-usable pieces of shipping information, relating to timing. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished (and identified/referenced) by their different values for [[transitTimeLabel]].

    Attributes:
        transitTimeLabel: Label to match an [[OfferShippingDetails]] with a [[DeliveryTimeSettings]] (within the context of a [[shippingSettingsLink]] cross-reference).
        isUnlabelledFallback: This can be marked 'true' to indicate that some published [[DeliveryTimeSettings]] or [[ShippingRateSettings]] are intended to apply to all [[OfferShippingDetails]] published by the same merchant, when referenced by a [[shippingSettingsLink]] in those settings. It is not meaningful to use a 'true' value for this property alongside a transitTimeLabel (for [[DeliveryTimeSettings]]) or shippingLabel (for [[ShippingRateSettings]]), since this property is for use with unlabelled settings.
        shippingDestination: indicates (possibly multiple) shipping destinations. These can be defined in several ways, e.g. postalCode ranges.
        deliveryTime: The total delay between the receipt of the order and the goods reaching the final customer.
    '''
    class_: Literal['https://schema.org/DeliveryTimeSettings'] = Field( # type: ignore
        default='https://schema.org/DeliveryTimeSettings',
        alias='@type',
        serialization_alias='@type'
    )
    transitTimeLabel: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'transitTimeLabel',
            'https://schema.org/transitTimeLabel'
        ),
        serialization_alias='https://schema.org/transitTimeLabel'
    )
    isUnlabelledFallback: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isUnlabelledFallback',
            'https://schema.org/isUnlabelledFallback'
        ),
        serialization_alias='https://schema.org/isUnlabelledFallback'
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
