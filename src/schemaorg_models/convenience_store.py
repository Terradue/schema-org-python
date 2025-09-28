from __future__ import annotations

from .store import Store    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ConvenienceStore(Store):
    """
A convenience store.
    """
    class_: Literal['https://schema.org/ConvenienceStore'] = Field( # type: ignore
        default='https://schema.org/ConvenienceStore',
        alias='@type',
        serialization_alias='@type'
    )
