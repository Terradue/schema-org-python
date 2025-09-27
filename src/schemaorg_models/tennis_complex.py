from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.sports_activity_location import SportsActivityLocation


class TennisComplex(SportsActivityLocation):
    """
A tennis complex.
    """
    type_: Literal['https://schema.org/TennisComplex'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TennisComplex'),serialization_alias='class') # type: ignore
