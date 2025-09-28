from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class WarrantyScope(Enumeration):
    """
The scope of the warranty promise.
    """
    class_: Literal['https://schema.org/WarrantyScope'] = Field( # type: ignore
        default='https://schema.org/WarrantyScope',
        alias='@type',
        serialization_alias='@type'
    )
