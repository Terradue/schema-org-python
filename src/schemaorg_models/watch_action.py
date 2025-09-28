from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .consume_action import ConsumeAction

class WatchAction(ConsumeAction):
    """
The act of consuming dynamic/moving visual content.
    """
    class_: Literal['https://schema.org/WatchAction'] = Field( # type: ignore
        default='https://schema.org/WatchAction',
        alias='@type',
        serialization_alias='@type'
    )
