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
from .event import Event
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .person import Person
    from .schedule import Schedule

class CourseInstance(Event):
    '''
    An instance of a [[Course]] which is distinct from other instances because it is offered at a different time or location or through different media or modes of study or to a specific section of students.

    Attributes:
        instructor: A person assigned to instruct or provide instructional assistance for the [[CourseInstance]].
        courseWorkload: The amount of work expected of students taking the course, often provided as a figure per week or per month, and may be broken down by type. For example, "2 hours of lectures, 1 hour of lab work and 3 hours of independent study per week".
        courseSchedule: Represents the length and pace of a course, expressed as a [[Schedule]].
        courseMode: The medium or means of delivery of the course instance or the mode of study, either as a text label (e.g. "online", "onsite" or "blended"; "synchronous" or "asynchronous"; "full-time" or "part-time") or as a URL reference to a term from a controlled vocabulary (e.g. https://ceds.ed.gov/element/001311#Asynchronous).
    '''
    class_: Literal['https://schema.org/CourseInstance'] = Field( # type: ignore
        default='https://schema.org/CourseInstance',
        alias='@type',
        serialization_alias='@type'
    )
    instructor: Optional[Union['Person', List['Person']]] = Field(
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
    courseSchedule: Optional[Union['Schedule', List['Schedule']]] = Field(
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
