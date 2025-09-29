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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .place import Place
    from .postal_address import PostalAddress
    from .thing import Thing
    from .quantitative_value import QuantitativeValue

class Game(CreativeWork):
    '''
    The Game type represents things which are games. These are typically rule-governed recreational activities, e.g. role-playing games in which players assume the role of characters in a fictional setting.

    Attributes:
        quest: The task that a player-controlled character, or group of characters may complete in order to gain a reward.
        characterAttribute: A piece of data that represents a particular aspect of a fictional character (skill, power, character points, advantage, disadvantage).
        gameItem: An item is an object within the game world that can be collected by a player or, occasionally, a non-player character.
        numberOfPlayers: Indicate how many people can play this game (minimum, maximum, or range).
        gameLocation: Real or fictional location of the game (or part of game).
    '''
    class_: Literal['https://schema.org/Game'] = Field( # type: ignore
        default='https://schema.org/Game',
        alias='@type',
        serialization_alias='@type'
    )
    quest: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    characterAttribute: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    gameItem: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    numberOfPlayers: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    gameLocation: Optional[Union['Place', List['Place'], HttpUrl, List[HttpUrl], 'PostalAddress', List['PostalAddress']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
