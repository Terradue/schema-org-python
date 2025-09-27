from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class GamePlayMode(Enumeration):
    """
Indicates whether this game is multi-player, co-op or single-player.
    """
    type_: Literal['https://schema.org/GamePlayMode'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/GamePlayMode'),serialization_alias='class') # type: ignore
