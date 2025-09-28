from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SizeGroupEnumeration(Enumeration):
    """
Enumerates common size groups for various product categories.
    """
    class_: Literal['https://schema.org/SizeGroupEnumeration'] = Field( # type: ignore
        default='https://schema.org/SizeGroupEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
