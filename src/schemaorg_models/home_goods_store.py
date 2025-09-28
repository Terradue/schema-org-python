from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class HomeGoodsStore(Store):
    """
A home goods store.
    """
    class_: Literal['https://schema.org/HomeGoodsStore'] = Field( # type: ignore
        default='https://schema.org/HomeGoodsStore',
        alias='@type',
        serialization_alias='@type'
    )
