from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PriceTypeEnumeration(Enumeration):
    """
Enumerates different price types, for example list price, invoice price, and sale price.
    """
    class_: Literal['https://schema.org/PriceTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/PriceTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
