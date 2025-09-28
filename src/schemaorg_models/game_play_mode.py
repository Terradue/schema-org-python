from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class GamePlayMode(Enumeration):
    """
Indicates whether this game is multi-player, co-op or single-player.
    """
    class_: Literal['https://schema.org/GamePlayMode'] = Field( # type: ignore
        default='https://schema.org/GamePlayMode',
        alias='@type',
        serialization_alias='@type'
    )
