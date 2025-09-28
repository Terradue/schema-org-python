from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .nonprofit_type import NonprofitType

class USNonprofitType(NonprofitType):
    """
USNonprofitType: Non-profit organization type originating from the United States.
    """
    class_: Literal['https://schema.org/USNonprofitType'] = Field( # type: ignore
        default='https://schema.org/USNonprofitType',
        alias='@type',
        serialization_alias='@type'
    )
