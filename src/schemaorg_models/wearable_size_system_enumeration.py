from __future__ import annotations

from .size_system_enumeration import SizeSystemEnumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class WearableSizeSystemEnumeration(SizeSystemEnumeration):
    """
Enumerates common size systems specific for wearable products.
    """
    class_: Literal['https://schema.org/WearableSizeSystemEnumeration'] = Field( # type: ignore
        default='https://schema.org/WearableSizeSystemEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
