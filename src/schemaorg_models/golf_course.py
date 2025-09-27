from typing import Literal
from pydantic import Field
from schemaorg_models.sports_activity_location import SportsActivityLocation


class GolfCourse(SportsActivityLocation):
    """
A golf course.
    """
    class_: Literal['https://schema.org/GolfCourse'] = Field('class', alias='class', serialization_alias='class') # type: ignore
