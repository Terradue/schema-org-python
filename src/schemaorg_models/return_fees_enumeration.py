from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ReturnFeesEnumeration(Enumeration):
    """
Enumerates several kinds of policies for product return fees.
    """
    class_: Literal['https://schema.org/ReturnFeesEnumeration'] = Field( # type: ignore
        default='https://schema.org/ReturnFeesEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
