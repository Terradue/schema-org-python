from __future__ import annotations

from .consume_action import ConsumeAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class WatchAction(ConsumeAction):
    """
The act of consuming dynamic/moving visual content.
    """
    class_: Literal['https://schema.org/WatchAction'] = Field( # type: ignore
        default='https://schema.org/WatchAction',
        alias='@type',
        serialization_alias='@type'
    )
