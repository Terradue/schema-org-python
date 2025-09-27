from typing import Literal
from pydantic import Field
from schemaorg_models.sports_activity_location import SportsActivityLocation


class BowlingAlley(SportsActivityLocation):
    """
A bowling alley.
    """
    class_: Literal['https://schema.org/BowlingAlley'] = Field('class', alias='class', serialization_alias='class') # type: ignore
