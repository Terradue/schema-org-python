from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ItemListOrderType(Enumeration):
    """
Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.
    """
    class_: Literal['https://schema.org/ItemListOrderType'] = Field( # type: ignore
        default='https://schema.org/ItemListOrderType',
        alias='@type',
        serialization_alias='@type'
    )
