from typing import Literal
from pydantic import Field
from schemaorg_models.sports_activity_location import SportsActivityLocation


class SportsClub(SportsActivityLocation):
    """
A sports club.
    """
    type_: Literal['https://schema.org/SportsClub'] = Field(default='https://schema.org/SportsClub', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
