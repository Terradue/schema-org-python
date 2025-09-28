from __future__ import annotations

from .consume_action import ConsumeAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class UseAction(ConsumeAction):
    """
The act of applying an object to its intended purpose.
    """
    class_: Literal['https://schema.org/UseAction'] = Field( # type: ignore
        default='https://schema.org/UseAction',
        alias='@type',
        serialization_alias='@type'
    )
