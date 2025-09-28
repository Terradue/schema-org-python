from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .broadcast_channel import BroadcastChannel

class TelevisionChannel(BroadcastChannel):
    """
A unique instance of a television BroadcastService on a CableOrSatelliteService lineup.
    """
    class_: Literal['https://schema.org/TelevisionChannel'] = Field( # type: ignore
        default='https://schema.org/TelevisionChannel',
        alias='@type',
        serialization_alias='@type'
    )
