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
    from .day_of_week import DayOfWeek
    from .service_period import ServicePeriod
    from .opening_hours_specification import OpeningHoursSpecification
    from .quantitative_value import QuantitativeValue

class ShippingDeliveryTime(StructuredValue):
    '''
    ShippingDeliveryTime provides various pieces of information about delivery times for shipping.

    Attributes:
        businessDays: Days of the week when the merchant typically operates, indicated via opening hours markup.
        transitTime: The typical delay the order has been sent for delivery and the goods reach the final customer.

  In the context of [[ShippingDeliveryTime]], use the [[QuantitativeValue]]. Typical properties: minValue, maxValue, unitCode (d for DAY).

  In the context of [[ShippingConditions]], use the [[ServicePeriod]]. It has a duration (as a [[QuantitativeValue]]) and also business days and a cut-off time.

        handlingTime: The typical delay between the receipt of the order and the goods either leaving the warehouse or being prepared for pickup, in case the delivery method is on site pickup.

In the context of [[ShippingDeliveryTime]], Typical properties: minValue, maxValue, unitCode (d for DAY).  This is by common convention assumed to mean business days (if a unitCode is used, coded as "d"), i.e. only counting days when the business normally operates.

In the context of [[ShippingService]], use the [[ServicePeriod]] format, that contains the same information in a structured form, with cut-off time, business days and duration.
        cutoffTime: Order cutoff time allows merchants to describe the time after which they will no longer process orders received on that day. For orders processed after cutoff time, one day gets added to the delivery time estimate. This property is expected to be most typically used via the [[ShippingRateSettings]] publication pattern. The time is indicated using the ISO-8601 Time format, e.g. "23:30:00-05:00" would represent 6:30 pm Eastern Standard Time (EST) which is 5 hours behind Coordinated Universal Time (UTC).
    '''
    class_: Literal['https://schema.org/ShippingDeliveryTime'] = Field( # type: ignore
        default='https://schema.org/ShippingDeliveryTime',
        alias='@type',
        serialization_alias='@type'
    )
    businessDays: Optional[Union['OpeningHoursSpecification', List['OpeningHoursSpecification'], 'DayOfWeek', List['DayOfWeek']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'businessDays',
            'https://schema.org/businessDays'
        ),
        serialization_alias='https://schema.org/businessDays'
    )
    transitTime: Optional[Union['ServicePeriod', List['ServicePeriod'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'transitTime',
            'https://schema.org/transitTime'
        ),
        serialization_alias='https://schema.org/transitTime'
    )
    handlingTime: Optional[Union['ServicePeriod', List['ServicePeriod'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
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
