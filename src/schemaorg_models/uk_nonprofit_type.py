from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .nonprofit_type import NonprofitType

class UKNonprofitType(NonprofitType):
    """
UKNonprofitType: Non-profit organization type originating from the United Kingdom.
    """
    class_: Literal['https://schema.org/UKNonprofitType'] = Field( # type: ignore
        default='https://schema.org/UKNonprofitType',
        alias='@type',
        serialization_alias='@type'
    )
