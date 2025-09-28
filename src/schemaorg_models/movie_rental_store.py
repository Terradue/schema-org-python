from __future__ import annotations

from .store import Store    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MovieRentalStore(Store):
    """
A movie rental store.
    """
    class_: Literal['https://schema.org/MovieRentalStore'] = Field( # type: ignore
        default='https://schema.org/MovieRentalStore',
        alias='@type',
        serialization_alias='@type'
    )
