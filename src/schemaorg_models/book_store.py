from __future__ import annotations

from .store import Store    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BookStore(Store):
    """
A bookstore.
    """
    class_: Literal['https://schema.org/BookStore'] = Field( # type: ignore
        default='https://schema.org/BookStore',
        alias='@type',
        serialization_alias='@type'
    )
