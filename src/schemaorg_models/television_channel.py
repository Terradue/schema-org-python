from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.broadcast_channel import BroadcastChannel

from pydantic import (
    Field
)
from typing import (
    Literal
)

class TelevisionChannel(BroadcastChannel):
    """
A unique instance of a television BroadcastService on a CableOrSatelliteService lineup.
    """
    class_: Literal['https://schema.org/TelevisionChannel'] = Field( # type: ignore
        default='https://schema.org/TelevisionChannel',
        alias='@type',
        serialization_alias='@type'
    )
