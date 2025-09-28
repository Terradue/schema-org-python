from __future__ import annotations

from .creative_work import CreativeWork    

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
from schemaorg_models.thing import Thing
from schemaorg_models.place import Place

class Game(CreativeWork):
    """
The Game type represents things which are games. These are typically rule-governed recreational activities, e.g. role-playing games in which players assume the role of characters in a fictional setting.
    """
    class_: Literal['https://schema.org/Game'] = Field( # type: ignore
        default='https://schema.org/Game',
        alias='@type',
        serialization_alias='@type'
    )
    quest: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'quest',
            'https://schema.org/quest'
        ),
        serialization_alias='https://schema.org/quest'
    )
    characterAttribute: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'characterAttribute',
            'https://schema.org/characterAttribute'
        ),
        serialization_alias='https://schema.org/characterAttribute'
    )
    gameItem: Optional[Union[Thing, List[Thing]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gameItem',
            'https://schema.org/gameItem'
        ),
        serialization_alias='https://schema.org/gameItem'
    )
    numberOfPlayers: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfPlayers',
            'https://schema.org/numberOfPlayers'
        ),
        serialization_alias='https://schema.org/numberOfPlayers'
    )
    gameLocation: Optional[Union[Place, List[Place], HttpUrl, List[HttpUrl], "PostalAddress", List["PostalAddress"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gameLocation',
            'https://schema.org/gameLocation'
        ),
        serialization_alias='https://schema.org/gameLocation'
    )
