from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.event import Event

from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.person import Person

class SportsEvent(Event):
    """
A sub property of location. The sports event where this action occurred.
    """
    class_: Literal['https://schema.org/SportsEvent'] = Field( # type: ignore
        default='https://schema.org/SportsEvent',
        alias='@type',
        serialization_alias='@type'
    )
    homeTeam: Optional[Union[Person, List[Person], "SportsTeam", List["SportsTeam"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'homeTeam',
            'https://schema.org/homeTeam'
        ),
        serialization_alias='https://schema.org/homeTeam'
    )
    awayTeam: Optional[Union["SportsTeam", List["SportsTeam"], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'awayTeam',
            'https://schema.org/awayTeam'
        ),
        serialization_alias='https://schema.org/awayTeam'
    )
    referee: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'referee',
            'https://schema.org/referee'
        ),
        serialization_alias='https://schema.org/referee'
    )
    sport: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sport',
            'https://schema.org/sport'
        ),
        serialization_alias='https://schema.org/sport'
    )
    competitor: Optional[Union["SportsTeam", List["SportsTeam"], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'competitor',
            'https://schema.org/competitor'
        ),
        serialization_alias='https://schema.org/competitor'
    )
