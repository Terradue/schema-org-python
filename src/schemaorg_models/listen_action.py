from __future__ import annotations

from .consume_action import ConsumeAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ListenAction(ConsumeAction):
    """
The act of consuming audio content.
    """
    class_: Literal['https://schema.org/ListenAction'] = Field( # type: ignore
        default='https://schema.org/ListenAction',
        alias='@type',
        serialization_alias='@type'
    )
