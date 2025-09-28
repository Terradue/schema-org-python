from __future__ import annotations

from .store import Store    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AutoPartsStore(Store):
    """
An auto parts store.
    """
    class_: Literal['https://schema.org/AutoPartsStore'] = Field( # type: ignore
        default='https://schema.org/AutoPartsStore',
        alias='@type',
        serialization_alias='@type'
    )
