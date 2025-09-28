from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class ProductReturnEnumeration(Enumeration):
    """
ProductReturnEnumeration enumerates several kinds of product return policy. Note that this structure may not capture all aspects of the policy.
    """
    class_: Literal['https://schema.org/ProductReturnEnumeration'] = Field( # type: ignore
        default='https://schema.org/ProductReturnEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
