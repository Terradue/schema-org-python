from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.status_enumeration import StatusEnumeration

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
