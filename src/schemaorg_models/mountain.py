from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .landform import Landform

class Mountain(Landform):
    """
A mountain, like Mount Whitney or Mount Everest.
    """
    class_: Literal['https://schema.org/Mountain'] = Field( # type: ignore
        default='https://schema.org/Mountain',
        alias='@type',
        serialization_alias='@type'
    )
