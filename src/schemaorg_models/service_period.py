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
    from .quantitative_value import QuantitativeValue
    from .duration import Duration
    from .day_of_week import DayOfWeek
    from .opening_hours_specification import OpeningHoursSpecification

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
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    duration: Optional[Union['Duration', List['Duration'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    cutoffTime: Optional[Union[time, List[time]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
