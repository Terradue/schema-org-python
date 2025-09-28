from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class HardwareStore(Store):
    """
A hardware store.
    """
    class_: Literal['https://schema.org/HardwareStore'] = Field( # type: ignore
        default='https://schema.org/HardwareStore',
        alias='@type',
        serialization_alias='@type'
    )
