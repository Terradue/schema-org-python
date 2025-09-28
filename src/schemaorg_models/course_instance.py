from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .event import Event
from .schedule import Schedule
from .person import Person

class CourseInstance(Event):
    """
An instance of a [[Course]] which is distinct from other instances because it is offered at a different time or location or through different media or modes of study or to a specific section of students.
    """
    class_: Literal['https://schema.org/CourseInstance'] = Field( # type: ignore
        default='https://schema.org/CourseInstance',
        alias='@type',
        serialization_alias='@type'
    )
    instructor: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'instructor',
            'https://schema.org/instructor'
        ),
        serialization_alias='https://schema.org/instructor'
    )
    courseWorkload: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'courseWorkload',
            'https://schema.org/courseWorkload'
        ),
        serialization_alias='https://schema.org/courseWorkload'
    )
    courseSchedule: Optional[Union[Schedule, List[Schedule]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'courseSchedule',
            'https://schema.org/courseSchedule'
        ),
        serialization_alias='https://schema.org/courseSchedule'
    )
    courseMode: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'courseMode',
            'https://schema.org/courseMode'
        ),
        serialization_alias='https://schema.org/courseMode'
    )
