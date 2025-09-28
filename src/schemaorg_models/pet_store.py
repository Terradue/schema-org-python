from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class PetStore(Store):
    """
A pet store.
    """
    class_: Literal['https://schema.org/PetStore'] = Field( # type: ignore
        default='https://schema.org/PetStore',
        alias='@type',
        serialization_alias='@type'
    )
