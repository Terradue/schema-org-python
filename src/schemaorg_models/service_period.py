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
    from .duration import Duration
    from .opening_hours_specification import OpeningHoursSpecification
    from .quantitative_value import QuantitativeValue

class ServicePeriod(StructuredValue):
    '''
    ServicePeriod represents a duration with some constraints about cutoff time and business days. This is used e.g. in shipping for handling times or transit time.

    Attributes:
        businessDays: Days of the week when the merchant typically operates, indicated via opening hours markup.
        duration: The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
        cutoffTime: Order cutoff time allows merchants to describe the time after which they will no longer process orders received on that day. For orders processed after cutoff time, one day gets added to the delivery time estimate. This property is expected to be most typically used via the [[ShippingRateSettings]] publication pattern. The time is indicated using the ISO-8601 Time format, e.g. "23:30:00-05:00" would represent 6:30 pm Eastern Standard Time (EST) which is 5 hours behind Coordinated Universal Time (UTC).
    '''
    class_: Literal['https://schema.org/ServicePeriod'] = Field( # type: ignore
        default='https://schema.org/ServicePeriod',
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
    duration: Optional[Union['Duration', List['Duration'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'duration',
            'https://schema.org/duration'
        ),
        serialization_alias='https://schema.org/duration'
    )
    cutoffTime: Optional[Union[time, List[time]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cutoffTime',
            'https://schema.org/cutoffTime'
        ),
        serialization_alias='https://schema.org/cutoffTime'
    )
