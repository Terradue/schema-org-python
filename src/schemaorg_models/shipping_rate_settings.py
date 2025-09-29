from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
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
    from .delivery_charge_specification import DeliveryChargeSpecification

class ShippingRateSettings(StructuredValue):
    """
A ShippingRateSettings represents re-usable pieces of shipping information. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished and matched (i.e. identified/referenced) by their different values for [[shippingLabel]].
    """
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
    freeShippingThreshold: Optional[Union["DeliveryChargeSpecification", List["DeliveryChargeSpecification"], "MonetaryAmount", List["MonetaryAmount"]]] = Field(
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
    shippingDestination: Optional[Union["DefinedRegion", List["DefinedRegion"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingDestination',
            'https://schema.org/shippingDestination'
        ),
        serialization_alias='https://schema.org/shippingDestination'
    )
    shippingRate: Optional[Union["ShippingRateSettings", List["ShippingRateSettings"], "MonetaryAmount", List["MonetaryAmount"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingRate',
            'https://schema.org/shippingRate'
        ),
        serialization_alias='https://schema.org/shippingRate'
    )
