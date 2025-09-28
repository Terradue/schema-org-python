from __future__ import annotations
from datetime import (
    time
)
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
    from .quantitative_value import QuantitativeValue
    from .opening_hours_specification import OpeningHoursSpecification
    from .service_period import ServicePeriod
    from .day_of_week import DayOfWeek

class ShippingDeliveryTime(StructuredValue):
    """
ShippingDeliveryTime provides various pieces of information about delivery times for shipping.
    """
    class_: Literal['https://schema.org/ShippingDeliveryTime'] = Field( # type: ignore
        default='https://schema.org/ShippingDeliveryTime',
        alias='@type',
        serialization_alias='@type'
    )
    businessDays: Optional[Union["OpeningHoursSpecification", List["OpeningHoursSpecification"], "DayOfWeek", List["DayOfWeek"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'businessDays',
            'https://schema.org/businessDays'
        ),
        serialization_alias='https://schema.org/businessDays'
    )
    transitTime: Optional[Union["ServicePeriod", List["ServicePeriod"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'transitTime',
            'https://schema.org/transitTime'
        ),
        serialization_alias='https://schema.org/transitTime'
    )
    handlingTime: Optional[Union["ServicePeriod", List["ServicePeriod"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'handlingTime',
            'https://schema.org/handlingTime'
        ),
        serialization_alias='https://schema.org/handlingTime'
    )
    cutoffTime: Optional[Union[time, List[time]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cutoffTime',
            'https://schema.org/cutoffTime'
        ),
        serialization_alias='https://schema.org/cutoffTime'
    )
