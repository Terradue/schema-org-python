from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MerchantReturnEnumeration(Enumeration):
    """
Enumerates several kinds of product return policies.
    """
    class_: Literal['https://schema.org/MerchantReturnEnumeration'] = Field( # type: ignore
        default='https://schema.org/MerchantReturnEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
