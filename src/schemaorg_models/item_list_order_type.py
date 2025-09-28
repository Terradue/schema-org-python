from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class ItemListOrderType(Enumeration):
    """
Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.
    """
    class_: Literal['https://schema.org/ItemListOrderType'] = Field( # type: ignore
        default='https://schema.org/ItemListOrderType',
        alias='@type',
        serialization_alias='@type'
    )
