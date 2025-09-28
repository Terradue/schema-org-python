from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class WholesaleStore(Store):
    """
A wholesale store.
    """
    class_: Literal['https://schema.org/WholesaleStore'] = Field( # type: ignore
        default='https://schema.org/WholesaleStore',
        alias='@type',
        serialization_alias='@type'
    )
