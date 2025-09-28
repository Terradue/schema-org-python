from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class PurchaseType(Enumeration):
    """
Optional. The type of purchase the consumer must make in order to qualify for this incentive.
    """
    class_: Literal['https://schema.org/PurchaseType'] = Field( # type: ignore
        default='https://schema.org/PurchaseType',
        alias='@type',
        serialization_alias='@type'
    )
