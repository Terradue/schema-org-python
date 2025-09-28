from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class RefundTypeEnumeration(Enumeration):
    """
Enumerates several kinds of product return refund types.
    """
    class_: Literal['https://schema.org/RefundTypeEnumeration'] = Field( # type: ignore
        default='https://schema.org/RefundTypeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
