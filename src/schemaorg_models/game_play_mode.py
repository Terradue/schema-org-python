from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class GamePlayMode(Enumeration):
    """
Indicates whether this game is multi-player, co-op or single-player.
    """
    class_: Literal['https://schema.org/GamePlayMode'] = Field('class', alias='class', serialization_alias='class') # type: ignore
