from __future__ import annotations
from datetime import (
    date,
    datetime,
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
    from .day_of_week import DayOfWeek

class OpeningHoursSpecification(StructuredValue):
    """
The opening hours of a certain place.
    """
    class_: Literal['https://schema.org/OpeningHoursSpecification'] = Field( # type: ignore
        default='https://schema.org/OpeningHoursSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    dayOfWeek: Optional[Union["DayOfWeek", List["DayOfWeek"]]] = Field(
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
