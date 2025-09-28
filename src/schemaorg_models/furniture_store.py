from __future__ import annotations

from .store import Store    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class FurnitureStore(Store):
    """
A furniture store.
    """
    class_: Literal['https://schema.org/FurnitureStore'] = Field( # type: ignore
        default='https://schema.org/FurnitureStore',
        alias='@type',
        serialization_alias='@type'
    )
