from typing import Literal
from pydantic import Field
from schemaorg_models.sports_activity_location import SportsActivityLocation


class GolfCourse(SportsActivityLocation):
    """
A golf course.
    """
    type_: Literal['https://schema.org/GolfCourse'] = Field(default='https://schema.org/GolfCourse', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
