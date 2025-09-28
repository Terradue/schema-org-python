from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class AutoPartsStore(Store):
    """
An auto parts store.
    """
    class_: Literal['https://schema.org/AutoPartsStore'] = Field( # type: ignore
        default='https://schema.org/AutoPartsStore',
        alias='@type',
        serialization_alias='@type'
    )
