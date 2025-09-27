from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.sports_activity_location import SportsActivityLocation


class GolfCourse(SportsActivityLocation):
    """
A golf course.
    """
    type_: Literal['https://schema.org/GolfCourse'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/GolfCourse'),serialization_alias='class') # type: ignore
