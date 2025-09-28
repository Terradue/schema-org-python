from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .consume_action import ConsumeAction

class DrinkAction(ConsumeAction):
    """
The act of swallowing liquids.
    """
    class_: Literal['https://schema.org/DrinkAction'] = Field( # type: ignore
        default='https://schema.org/DrinkAction',
        alias='@type',
        serialization_alias='@type'
    )
