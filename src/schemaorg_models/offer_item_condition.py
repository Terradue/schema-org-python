from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class OfferItemCondition(Enumeration):
    """
A list of possible conditions for the item.
    """
    class_: Literal['https://schema.org/OfferItemCondition'] = Field( # type: ignore
        default='https://schema.org/OfferItemCondition',
        alias='@type',
        serialization_alias='@type'
    )
