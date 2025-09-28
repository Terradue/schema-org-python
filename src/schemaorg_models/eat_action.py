from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .consume_action import ConsumeAction

class EatAction(ConsumeAction):
    """
The act of swallowing solid objects.
    """
    class_: Literal['https://schema.org/EatAction'] = Field( # type: ignore
        default='https://schema.org/EatAction',
        alias='@type',
        serialization_alias='@type'
    )
