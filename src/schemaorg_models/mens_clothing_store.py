from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class MensClothingStore(Store):
    """
A men's clothing store.
    """
    class_: Literal['https://schema.org/MensClothingStore'] = Field( # type: ignore
        default='https://schema.org/MensClothingStore',
        alias='@type',
        serialization_alias='@type'
    )
