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

class RadioChannel(BroadcastChannel):
    """
A unique instance of a radio BroadcastService on a CableOrSatelliteService lineup.
    """
    class_: Literal['https://schema.org/RadioChannel'] = Field( # type: ignore
        default='https://schema.org/RadioChannel',
        alias='@type',
        serialization_alias='@type'
    )
