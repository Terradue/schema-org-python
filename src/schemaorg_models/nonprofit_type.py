from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class NonprofitType(Enumeration):
    """
NonprofitType enumerates several kinds of official non-profit types of which a non-profit organization can be.
    """
    class_: Literal['https://schema.org/NonprofitType'] = Field( # type: ignore
        default='https://schema.org/NonprofitType',
        alias='@type',
        serialization_alias='@type'
    )
