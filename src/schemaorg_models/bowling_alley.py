from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.sports_activity_location import SportsActivityLocation


class BowlingAlley(SportsActivityLocation):
    """
A bowling alley.
    """
    type_: Literal['https://schema.org/BowlingAlley'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BowlingAlley'),serialization_alias='class') # type: ignore
