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

class OpeningHoursSpecification(StructuredValue):
    '''
    A structured value providing information about the opening hours of a place or a certain service inside a place.\
\

The place is __open__ if the [[opens]] property is specified, and __closed__ otherwise.\
\
If the value for the [[closes]] property is less than the value for the [[opens]] property then the hour range is assumed to span over the next day.
      

    Attributes:
        dayOfWeek: The day of the week for which these opening hours are valid.
        validFrom: The date when the item becomes valid.
        closes: The closing hour of the place or service on the given day(s) of the week.
        opens: The opening hour of the place or service on the given day(s) of the week.
        validThrough: The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
    '''
    class_: Literal['https://schema.org/OpeningHoursSpecification'] = Field( # type: ignore
        default='https://schema.org/OpeningHoursSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    dayOfWeek: Optional[Union['DayOfWeek', List['DayOfWeek']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dayOfWeek',
            'https://schema.org/dayOfWeek'
        ),
        serialization_alias='https://schema.org/dayOfWeek'
    )
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validFrom',
            'https://schema.org/validFrom'
        ),
        serialization_alias='https://schema.org/validFrom'
    )
    closes: Optional[Union[time, List[time]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'closes',
            'https://schema.org/closes'
        ),
        serialization_alias='https://schema.org/closes'
    )
    opens: Optional[Union[time, List[time]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'opens',
            'https://schema.org/opens'
        ),
        serialization_alias='https://schema.org/opens'
    )
    validThrough: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validThrough',
            'https://schema.org/validThrough'
        ),
        serialization_alias='https://schema.org/validThrough'
    )
