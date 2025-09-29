from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .event import Event
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .person import Person
    from .sports_team import SportsTeam

class SportsEvent(Event):
    '''
    Event type: Sports event.

    Attributes:
        homeTeam: The home team in a sports event.
        awayTeam: The away team in a sports event.
        referee: An official who watches a game or match closely to enforce the rules and arbitrate on matters arising from the play such as referees, umpires or judges. The name of the effective function can vary according to the sport.
        sport: A type of sport (e.g. Baseball).
        competitor: A competitor in a sports event.
    '''
    class_: Literal['https://schema.org/SportsEvent'] = Field( # type: ignore
        default='https://schema.org/SportsEvent',
        alias='@type',
        serialization_alias='@type'
    )
    homeTeam: Optional[Union['Person', List['Person'], 'SportsTeam', List['SportsTeam']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'homeTeam',
            'https://schema.org/homeTeam'
        ),
        serialization_alias='https://schema.org/homeTeam'
    )
    awayTeam: Optional[Union['SportsTeam', List['SportsTeam'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'awayTeam',
            'https://schema.org/awayTeam'
        ),
        serialization_alias='https://schema.org/awayTeam'
    )
    referee: Optional[Union['Person', List['Person']]] = Field(
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
    competitor: Optional[Union['SportsTeam', List['SportsTeam'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'competitor',
            'https://schema.org/competitor'
        ),
        serialization_alias='https://schema.org/competitor'
    )
