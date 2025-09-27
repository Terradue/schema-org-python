from typing import Literal
from pydantic import Field
from schemaorg_models.sports_activity_location import SportsActivityLocation


class BowlingAlley(SportsActivityLocation):
    """
A bowling alley.
    """
    class_: Literal['https://schema.org/BowlingAlley'] = Field(default='https://schema.org/BowlingAlley', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
