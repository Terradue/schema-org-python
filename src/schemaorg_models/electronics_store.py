from __future__ import annotations

from .store import Store    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ElectronicsStore(Store):
    """
An electronics store.
    """
    class_: Literal['https://schema.org/ElectronicsStore'] = Field( # type: ignore
        default='https://schema.org/ElectronicsStore',
        alias='@type',
        serialization_alias='@type'
    )
