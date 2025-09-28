from __future__ import annotations

from .store import Store    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ToyStore(Store):
    """
A toy store.
    """
    class_: Literal['https://schema.org/ToyStore'] = Field( # type: ignore
        default='https://schema.org/ToyStore',
        alias='@type',
        serialization_alias='@type'
    )
