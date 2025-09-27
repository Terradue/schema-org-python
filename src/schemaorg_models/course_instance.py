from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.event import Event

from schemaorg_models.person import Person

class CourseInstance(Event):
    """
An instance of a [[Course]] which is distinct from other instances because it is offered at a different time or location or through different media or modes of study or to a specific section of students.
    """
    class_: Literal['https://schema.org/CourseInstance'] = Field(default='https://schema.org/CourseInstance', alias='@type', serialization_alias='@type') # type: ignore
    instructor: Optional[Union[Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('instructor', 'https://schema.org/instructor'), serialization_alias='https://schema.org/instructor')
    courseWorkload: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('courseWorkload', 'https://schema.org/courseWorkload'), serialization_alias='https://schema.org/courseWorkload')
    courseSchedule: Optional[Union["Schedule", List["Schedule"]]] = Field(default=None, validation_alias=AliasChoices('courseSchedule', 'https://schema.org/courseSchedule'), serialization_alias='https://schema.org/courseSchedule')
    courseMode: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('courseMode', 'https://schema.org/courseMode'), serialization_alias='https://schema.org/courseMode')
    @field_serializer('courseMode')
    def courseMode2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

