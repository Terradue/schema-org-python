from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class MovieRentalStore(Store):
    """
A movie rental store.
    """
    class_: Literal['https://schema.org/MovieRentalStore'] = Field( # type: ignore
        default='https://schema.org/MovieRentalStore',
        alias='@type',
        serialization_alias='@type'
    )
