from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .assess_action import AssessAction

class ReactAction(AssessAction):
    """
The act of responding instinctively and emotionally to an object, expressing a sentiment.
    """
    class_: Literal['https://schema.org/ReactAction'] = Field( # type: ignore
        default='https://schema.org/ReactAction',
        alias='@type',
        serialization_alias='@type'
    )
