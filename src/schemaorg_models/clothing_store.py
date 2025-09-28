from __future__ import annotations

from .store import Store    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ClothingStore(Store):
    """
A clothing store.
    """
    class_: Literal['https://schema.org/ClothingStore'] = Field( # type: ignore
        default='https://schema.org/ClothingStore',
        alias='@type',
        serialization_alias='@type'
    )
