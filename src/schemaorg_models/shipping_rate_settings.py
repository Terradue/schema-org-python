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
    from .delivery_charge_specification import DeliveryChargeSpecification
    from .monetary_amount import MonetaryAmount
    from .defined_region import DefinedRegion

class ShippingRateSettings(StructuredValue):
    '''
    A ShippingRateSettings represents re-usable pieces of shipping information. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished and matched (i.e. identified/referenced) by their different values for [[shippingLabel]].

    Attributes:
        weightPercentage: Fraction of the weight that is used to compute the shipping price.
        doesNotShip: Indicates when shipping to a particular [[shippingDestination]] is not available.
        freeShippingThreshold: A monetary value above (or at) which the shipping rate becomes free. Intended to be used via an [[OfferShippingDetails]] with [[shippingSettingsLink]] matching this [[ShippingRateSettings]].
        isUnlabelledFallback: This can be marked 'true' to indicate that some published [[DeliveryTimeSettings]] or [[ShippingRateSettings]] are intended to apply to all [[OfferShippingDetails]] published by the same merchant, when referenced by a [[shippingSettingsLink]] in those settings. It is not meaningful to use a 'true' value for this property alongside a transitTimeLabel (for [[DeliveryTimeSettings]]) or shippingLabel (for [[ShippingRateSettings]]), since this property is for use with unlabelled settings.
        orderPercentage: Fraction of the value of the order that is charged as shipping cost.
        shippingLabel: Label to match an [[OfferShippingDetails]] with a [[ShippingRateSettings]] (within the context of a [[shippingSettingsLink]] cross-reference).
        shippingDestination: indicates (possibly multiple) shipping destinations. These can be defined in several ways, e.g. postalCode ranges.
        shippingRate: The shipping rate is the cost of shipping to the specified destination. Typically, the maxValue and currency values (of the [[MonetaryAmount]]) are most appropriate.
    '''
    class_: Literal['https://schema.org/ShippingRateSettings'] = Field( # type: ignore
        default='https://schema.org/ShippingRateSettings',
        alias='@type',
        serialization_alias='@type'
    )
    weightPercentage: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'weightPercentage',
            'https://schema.org/weightPercentage'
        ),
        serialization_alias='https://schema.org/weightPercentage'
    )
    doesNotShip: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'doesNotShip',
            'https://schema.org/doesNotShip'
        ),
        serialization_alias='https://schema.org/doesNotShip'
    )
    freeShippingThreshold: Optional[Union['DeliveryChargeSpecification', List['DeliveryChargeSpecification'], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'freeShippingThreshold',
            'https://schema.org/freeShippingThreshold'
        ),
        serialization_alias='https://schema.org/freeShippingThreshold'
    )
    isUnlabelledFallback: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isUnlabelledFallback',
            'https://schema.org/isUnlabelledFallback'
        ),
        serialization_alias='https://schema.org/isUnlabelledFallback'
    )
    orderPercentage: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'orderPercentage',
            'https://schema.org/orderPercentage'
        ),
        serialization_alias='https://schema.org/orderPercentage'
    )
    shippingLabel: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingLabel',
            'https://schema.org/shippingLabel'
        ),
        serialization_alias='https://schema.org/shippingLabel'
    )
    shippingDestination: Optional[Union['DefinedRegion', List['DefinedRegion']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingDestination',
            'https://schema.org/shippingDestination'
        ),
        serialization_alias='https://schema.org/shippingDestination'
    )
    shippingRate: Optional[Union['ShippingRateSettings', List['ShippingRateSettings'], 'MonetaryAmount', List['MonetaryAmount']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingRate',
            'https://schema.org/shippingRate'
        ),
        serialization_alias='https://schema.org/shippingRate'
    )
