from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class SportingGoodsStore(Store):
    """
A sporting goods store.
    """
    class_: Literal['https://schema.org/SportingGoodsStore'] = Field( # type: ignore
        default='https://schema.org/SportingGoodsStore',
        alias='@type',
        serialization_alias='@type'
    )
