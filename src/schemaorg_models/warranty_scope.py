from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class WarrantyScope(Enumeration):
    """
The scope of the warranty promise.
    """
    class_: Literal['https://schema.org/WarrantyScope'] = Field( # type: ignore
        default='https://schema.org/WarrantyScope',
        alias='@type',
        serialization_alias='@type'
    )
