from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class ReturnFeesEnumeration(Enumeration):
    """
Enumerates several kinds of policies for product return fees.
    """
    class_: Literal['https://schema.org/ReturnFeesEnumeration'] = Field( # type: ignore
        default='https://schema.org/ReturnFeesEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
