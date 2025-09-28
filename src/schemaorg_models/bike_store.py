from __future__ import annotations

from .store import Store    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BikeStore(Store):
    """
A bike store.
    """
    class_: Literal['https://schema.org/BikeStore'] = Field( # type: ignore
        default='https://schema.org/BikeStore',
        alias='@type',
        serialization_alias='@type'
    )
