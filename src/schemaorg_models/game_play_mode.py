from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class GamePlayMode(Enumeration):
    """
Indicates whether this game is multi-player, co-op or single-player.
    """
    type_: Literal['https://schema.org/GamePlayMode'] = Field(default='https://schema.org/GamePlayMode', alias='@type', serialization_alias='@type') # type: ignore
