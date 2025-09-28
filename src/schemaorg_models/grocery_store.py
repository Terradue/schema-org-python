from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class GroceryStore(Store):
    """
A grocery store.
    """
    class_: Literal['https://schema.org/GroceryStore'] = Field( # type: ignore
        default='https://schema.org/GroceryStore',
        alias='@type',
        serialization_alias='@type'
    )
