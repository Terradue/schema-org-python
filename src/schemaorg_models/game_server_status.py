from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .status_enumeration import StatusEnumeration

class GameServerStatus(StatusEnumeration):
    """
Status of a game server.
    """
    class_: Literal['https://schema.org/GameServerStatus'] = Field( # type: ignore
        default='https://schema.org/GameServerStatus',
        alias='@type',
        serialization_alias='@type'
    )
