from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ReturnMethodEnumeration(Enumeration):
    """
Enumerates several types of product return methods.
    """
    class_: Literal['https://schema.org/ReturnMethodEnumeration'] = Field( # type: ignore
        default='https://schema.org/ReturnMethodEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
