from __future__ import annotations

from .status_enumeration import StatusEnumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class OrderStatus(StatusEnumeration):
    """
Enumerated status values for Order.
    """
    class_: Literal['https://schema.org/OrderStatus'] = Field( # type: ignore
        default='https://schema.org/OrderStatus',
        alias='@type',
        serialization_alias='@type'
    )
