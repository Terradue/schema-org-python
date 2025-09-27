from typing import Literal
from pydantic import Field
from schemaorg_models.sports_activity_location import SportsActivityLocation


class TennisComplex(SportsActivityLocation):
    """
A tennis complex.
    """
    class_: Literal['https://schema.org/TennisComplex'] = Field(default='https://schema.org/TennisComplex', alias='class', serialization_alias='class') # type: ignore
