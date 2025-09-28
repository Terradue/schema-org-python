from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class DeliveryMethod(Enumeration):
    """
A sub property of instrument. The method of delivery.
    """
    class_: Literal['https://schema.org/DeliveryMethod'] = Field( # type: ignore
        default='https://schema.org/DeliveryMethod',
        alias='@type',
        serialization_alias='@type'
    )
