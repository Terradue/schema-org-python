from __future__ import annotations

from .store import Store    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class HardwareStore(Store):
    """
A hardware store.
    """
    class_: Literal['https://schema.org/HardwareStore'] = Field( # type: ignore
        default='https://schema.org/HardwareStore',
        alias='@type',
        serialization_alias='@type'
    )
