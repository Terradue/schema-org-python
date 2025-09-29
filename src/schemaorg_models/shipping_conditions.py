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
    from .service_period import ServicePeriod
    from .quantitative_value import QuantitativeValue
    from .mass import Mass
    from .opening_hours_specification import OpeningHoursSpecification
    from .monetary_amount import MonetaryAmount
    from .defined_region import DefinedRegion
    from .distance import Distance
    from .shipping_rate_settings import ShippingRateSettings

class ShippingConditions(StructuredValue):
    """
The conditions (constraints, price) applicable to the [[ShippingService]].
    """
    class_: Literal['https://schema.org/ShippingConditions'] = Field( # type: ignore
        default='https://schema.org/ShippingConditions',
        alias='@type',
        serialization_alias='@type'
    )
    weight: Optional[Union["QuantitativeValue", List["QuantitativeValue"], "Mass", List["Mass"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'weight',
            'https://schema.org/weight'
        ),
        serialization_alias='https://schema.org/weight'
    )
    shippingOrigin: Optional[Union["DefinedRegion", List["DefinedRegion"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingOrigin',
            'https://schema.org/shippingOrigin'
        ),
        serialization_alias='https://schema.org/shippingOrigin'
    )
    shippingDestination: Optional[Union["DefinedRegion", List["DefinedRegion"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingDestination',
            'https://schema.org/shippingDestination'
        ),
        serialization_alias='https://schema.org/shippingDestination'
    )
    seasonalOverride: Optional[Union["OpeningHoursSpecification", List["OpeningHoursSpecification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seasonalOverride',
            'https://schema.org/seasonalOverride'
        ),
        serialization_alias='https://schema.org/seasonalOverride'
    )
    shippingRate: Optional[Union["ShippingRateSettings", List["ShippingRateSettings"], "MonetaryAmount", List["MonetaryAmount"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingRate',
            'https://schema.org/shippingRate'
        ),
        serialization_alias='https://schema.org/shippingRate'
    )
    depth: Optional[Union["Distance", List["Distance"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
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
    width: Optional[Union["QuantitativeValue", List["QuantitativeValue"], "Distance", List["Distance"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'width',
            'https://schema.org/width'
        ),
        serialization_alias='https://schema.org/width'
    )
    numItems: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numItems',
            'https://schema.org/numItems'
        ),
        serialization_alias='https://schema.org/numItems'
    )
    orderValue: Optional[Union["MonetaryAmount", List["MonetaryAmount"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'orderValue',
            'https://schema.org/orderValue'
        ),
        serialization_alias='https://schema.org/orderValue'
    )
    transitTime: Optional[Union["ServicePeriod", List["ServicePeriod"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'transitTime',
            'https://schema.org/transitTime'
        ),
        serialization_alias='https://schema.org/transitTime'
    )
    height: Optional[Union["Distance", List["Distance"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'height',
            'https://schema.org/height'
        ),
        serialization_alias='https://schema.org/height'
    )
