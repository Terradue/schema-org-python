from __future__ import annotations

from .intangible import Intangible    

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

class Schedule(Intangible):
    """
A schedule defines a repeating time period used to describe a regularly occurring [[Event]]. At a minimum a schedule will specify [[repeatFrequency]] which describes the interval between occurrences of the event. Additional information can be provided to specify the schedule more precisely.
      This includes identifying the day(s) of the week or month when the recurring event will take place, in addition to its start and end time. Schedules may also
      have start and end dates to indicate when they are active, e.g. to define a limited calendar of events.
    """
    class_: Literal['https://schema.org/Schedule'] = Field( # type: ignore
        default='https://schema.org/Schedule',
        alias='@type',
        serialization_alias='@type'
    )
    scheduleTimezone: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'scheduleTimezone',
            'https://schema.org/scheduleTimezone'
        ),
        serialization_alias='https://schema.org/scheduleTimezone'
    )
    repeatFrequency: Optional[Union[str, List[str], "Duration", List["Duration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'repeatFrequency',
            'https://schema.org/repeatFrequency'
        ),
        serialization_alias='https://schema.org/repeatFrequency'
    )
    endDate: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'endDate',
            'https://schema.org/endDate'
        ),
        serialization_alias='https://schema.org/endDate'
    )
    exceptDate: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'exceptDate',
            'https://schema.org/exceptDate'
        ),
        serialization_alias='https://schema.org/exceptDate'
    )
    byDay: Optional[Union[str, List[str], "DayOfWeek", List["DayOfWeek"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'byDay',
            'https://schema.org/byDay'
        ),
        serialization_alias='https://schema.org/byDay'
    )
    byMonthDay: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'byMonthDay',
            'https://schema.org/byMonthDay'
        ),
        serialization_alias='https://schema.org/byMonthDay'
    )
    endTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'endTime',
            'https://schema.org/endTime'
        ),
        serialization_alias='https://schema.org/endTime'
    )
    startDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'startDate',
            'https://schema.org/startDate'
        ),
        serialization_alias='https://schema.org/startDate'
    )
    duration: Optional[Union["Duration", List["Duration"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'duration',
            'https://schema.org/duration'
        ),
        serialization_alias='https://schema.org/duration'
    )
    repeatCount: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'repeatCount',
            'https://schema.org/repeatCount'
        ),
        serialization_alias='https://schema.org/repeatCount'
    )
    byMonthWeek: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'byMonthWeek',
            'https://schema.org/byMonthWeek'
        ),
        serialization_alias='https://schema.org/byMonthWeek'
    )
    byMonth: Optional[Union[int, List[int]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'byMonth',
            'https://schema.org/byMonth'
        ),
        serialization_alias='https://schema.org/byMonth'
    )
    startTime: Optional[Union[time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'startTime',
            'https://schema.org/startTime'
        ),
        serialization_alias='https://schema.org/startTime'
    )
