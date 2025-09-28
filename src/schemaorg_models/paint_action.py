from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .create_action import CreateAction

class PaintAction(CreateAction):
    """
The act of producing a painting, typically with paint and canvas as instruments.
    """
    class_: Literal['https://schema.org/PaintAction'] = Field( # type: ignore
        default='https://schema.org/PaintAction',
        alias='@type',
        serialization_alias='@type'
    )
