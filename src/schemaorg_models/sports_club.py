from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.sports_activity_location import SportsActivityLocation


class SportsClub(SportsActivityLocation):
    """
A sports club.
    """
    type_: Literal['https://schema.org/SportsClub'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SportsClub'),serialization_alias='class') # type: ignore
