from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class ElectronicsStore(Store):
    """
An electronics store.
    """
    class_: Literal['https://schema.org/ElectronicsStore'] = Field( # type: ignore
        default='https://schema.org/ElectronicsStore',
        alias='@type',
        serialization_alias='@type'
    )
