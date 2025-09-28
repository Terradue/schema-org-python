from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class Florist(Store):
    """
A florist.
    """
    class_: Literal['https://schema.org/Florist'] = Field( # type: ignore
        default='https://schema.org/Florist',
        alias='@type',
        serialization_alias='@type'
    )
