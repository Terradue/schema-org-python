from __future__ import annotations

from .broadcast_channel import BroadcastChannel    

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
