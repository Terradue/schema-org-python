from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.enumeration import Enumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class GamePlayMode(Enumeration):
    """
Indicates whether this game is multi-player, co-op or single-player.
    """
    class_: Literal['https://schema.org/GamePlayMode'] = Field( # type: ignore
        default='https://schema.org/GamePlayMode',
        alias='@type',
        serialization_alias='@type'
    )
