from __future__ import annotations

from .broadcast_service import BroadcastService    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class RadioBroadcastService(BroadcastService):
    """
A delivery service through which radio content is provided via broadcast over the air or online.
    """
    class_: Literal['https://schema.org/RadioBroadcastService'] = Field( # type: ignore
        default='https://schema.org/RadioBroadcastService',
        alias='@type',
        serialization_alias='@type'
    )
