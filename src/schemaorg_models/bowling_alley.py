from typing import Literal
from pydantic import Field
from schemaorg_models.sports_activity_location import SportsActivityLocation


class BowlingAlley(SportsActivityLocation):
    """
A bowling alley.
    """
    type_: Literal['https://schema.org/BowlingAlley'] = Field(default='https://schema.org/BowlingAlley', alias='@type', serialization_alias='@type') # type: ignore
