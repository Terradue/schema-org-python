from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class ClothingStore(Store):
    """
A clothing store.
    """
    class_: Literal['https://schema.org/ClothingStore'] = Field( # type: ignore
        default='https://schema.org/ClothingStore',
        alias='@type',
        serialization_alias='@type'
    )
