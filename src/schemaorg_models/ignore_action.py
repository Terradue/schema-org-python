from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .assess_action import AssessAction

class IgnoreAction(AssessAction):
    """
The act of intentionally disregarding the object. An agent ignores an object.
    """
    class_: Literal['https://schema.org/IgnoreAction'] = Field( # type: ignore
        default='https://schema.org/IgnoreAction',
        alias='@type',
        serialization_alias='@type'
    )
