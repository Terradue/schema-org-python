from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class JewelryStore(Store):
    """
A jewelry store.
    """
    class_: Literal['https://schema.org/JewelryStore'] = Field( # type: ignore
        default='https://schema.org/JewelryStore',
        alias='@type',
        serialization_alias='@type'
    )
