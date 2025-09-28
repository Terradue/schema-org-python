from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class GardenStore(Store):
    """
A garden store.
    """
    class_: Literal['https://schema.org/GardenStore'] = Field( # type: ignore
        default='https://schema.org/GardenStore',
        alias='@type',
        serialization_alias='@type'
    )
