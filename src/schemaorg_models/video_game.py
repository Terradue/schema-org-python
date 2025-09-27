from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.game import Game

from schemaorg_models.creative_work import CreativeWork
from schemaorg_models.person import Person
from schemaorg_models.thing import Thing
from schemaorg_models.game_server import GameServer
from schemaorg_models.performing_group import PerformingGroup
from schemaorg_models.game_play_mode import GamePlayMode

class VideoGame(Game):
    """
A video game is an electronic game that involves human interaction with a user interface to generate visual feedback on a video device.
    """
    type_: Literal['https://schema.org/VideoGame'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/VideoGame'),serialization_alias='class') # type: ignore
    gameTip: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(default=None,validation_alias=AliasChoices('gameTip', 'https://schema.org/gameTip'),serialization_alias='https://schema.org/gameTip')
    musicBy: Optional[Union["MusicGroup", List["MusicGroup"], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('musicBy', 'https://schema.org/musicBy'),serialization_alias='https://schema.org/musicBy')
    gamePlatform: Optional[Union[HttpUrl, List[HttpUrl], str, List[str], Thing, List[Thing]]] = Field(default=None,validation_alias=AliasChoices('gamePlatform', 'https://schema.org/gamePlatform'),serialization_alias='https://schema.org/gamePlatform')
    @field_serializer('gamePlatform')
    def gamePlatform2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    cheatCode: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(default=None,validation_alias=AliasChoices('cheatCode', 'https://schema.org/cheatCode'),serialization_alias='https://schema.org/cheatCode')
    trailer: Optional[Union["VideoObject", List["VideoObject"]]] = Field(default=None,validation_alias=AliasChoices('trailer', 'https://schema.org/trailer'),serialization_alias='https://schema.org/trailer')
    directors: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('directors', 'https://schema.org/directors'),serialization_alias='https://schema.org/directors')
    director: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('director', 'https://schema.org/director'),serialization_alias='https://schema.org/director')
    gameServer: Optional[Union[GameServer, List[GameServer]]] = Field(default=None,validation_alias=AliasChoices('gameServer', 'https://schema.org/gameServer'),serialization_alias='https://schema.org/gameServer')
    actor: Optional[Union[Person, List[Person], PerformingGroup, List[PerformingGroup]]] = Field(default=None,validation_alias=AliasChoices('actor', 'https://schema.org/actor'),serialization_alias='https://schema.org/actor')
    playMode: Optional[Union[GamePlayMode, List[GamePlayMode]]] = Field(default=None,validation_alias=AliasChoices('playMode', 'https://schema.org/playMode'),serialization_alias='https://schema.org/playMode')
    gameEdition: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('gameEdition', 'https://schema.org/gameEdition'),serialization_alias='https://schema.org/gameEdition')
    actors: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('actors', 'https://schema.org/actors'),serialization_alias='https://schema.org/actors')
