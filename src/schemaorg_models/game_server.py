from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class GameServer(Intangible):
    """
Server that provides game interaction in a multiplayer game.
    """
    class_: Literal['https://schema.org/GameServer'] = Field(default='https://schema.org/GameServer', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    playersOnline: Optional[Union[int, List[int]]] = Field(default=None, validation_alias=AliasChoices('playersOnline', 'https://schema.org/playersOnline'), serialization_alias='https://schema.org/playersOnline')
    serverStatus: Optional[Union["GameServerStatus", List["GameServerStatus"]]] = Field(default=None, validation_alias=AliasChoices('serverStatus', 'https://schema.org/serverStatus'), serialization_alias='https://schema.org/serverStatus')
    game: Optional[Union["VideoGame", List["VideoGame"]]] = Field(default=None, validation_alias=AliasChoices('game', 'https://schema.org/game'), serialization_alias='https://schema.org/game')
