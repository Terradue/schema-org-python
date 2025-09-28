from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class TireShop(Store):
    """
A tire shop.
    """
    class_: Literal['https://schema.org/TireShop'] = Field( # type: ignore
        default='https://schema.org/TireShop',
        alias='@type',
        serialization_alias='@type'
    )
