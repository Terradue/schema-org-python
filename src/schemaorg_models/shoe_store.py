from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class ShoeStore(Store):
    """
A shoe store.
    """
    class_: Literal['https://schema.org/ShoeStore'] = Field( # type: ignore
        default='https://schema.org/ShoeStore',
        alias='@type',
        serialization_alias='@type'
    )
