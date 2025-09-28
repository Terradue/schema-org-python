from __future__ import annotations

from .consume_action import ConsumeAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DrinkAction(ConsumeAction):
    """
The act of swallowing liquids.
    """
    class_: Literal['https://schema.org/DrinkAction'] = Field( # type: ignore
        default='https://schema.org/DrinkAction',
        alias='@type',
        serialization_alias='@type'
    )
