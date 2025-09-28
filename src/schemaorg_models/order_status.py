from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .status_enumeration import StatusEnumeration

class OrderStatus(StatusEnumeration):
    """
Enumerated status values for Order.
    """
    class_: Literal['https://schema.org/OrderStatus'] = Field( # type: ignore
        default='https://schema.org/OrderStatus',
        alias='@type',
        serialization_alias='@type'
    )
