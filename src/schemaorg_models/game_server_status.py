from __future__ import annotations

from .status_enumeration import StatusEnumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class GameServerStatus(StatusEnumeration):
    """
Status of a game server.
    """
    class_: Literal['https://schema.org/GameServerStatus'] = Field( # type: ignore
        default='https://schema.org/GameServerStatus',
        alias='@type',
        serialization_alias='@type'
    )
