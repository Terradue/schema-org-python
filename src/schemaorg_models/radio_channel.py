from __future__ import annotations

from .broadcast_channel import BroadcastChannel    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class RadioChannel(BroadcastChannel):
    """
A unique instance of a radio BroadcastService on a CableOrSatelliteService lineup.
    """
    class_: Literal['https://schema.org/RadioChannel'] = Field( # type: ignore
        default='https://schema.org/RadioChannel',
        alias='@type',
        serialization_alias='@type'
    )
