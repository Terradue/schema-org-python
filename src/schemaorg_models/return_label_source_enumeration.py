from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class ReturnLabelSourceEnumeration(Enumeration):
    """
Enumerates several types of return labels for product returns.
    """
    class_: Literal['https://schema.org/ReturnLabelSourceEnumeration'] = Field( # type: ignore
        default='https://schema.org/ReturnLabelSourceEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
