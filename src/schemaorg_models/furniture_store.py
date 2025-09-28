from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class FurnitureStore(Store):
    """
A furniture store.
    """
    class_: Literal['https://schema.org/FurnitureStore'] = Field( # type: ignore
        default='https://schema.org/FurnitureStore',
        alias='@type',
        serialization_alias='@type'
    )
