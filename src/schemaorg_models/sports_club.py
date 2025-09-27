from typing import Literal
from pydantic import Field
from schemaorg_models.sports_activity_location import SportsActivityLocation


class SportsClub(SportsActivityLocation):
    """
A sports club.
    """
    class_: Literal['https://schema.org/SportsClub'] = Field(default='https://schema.org/SportsClub', alias='class', serialization_alias='class') # type: ignore
