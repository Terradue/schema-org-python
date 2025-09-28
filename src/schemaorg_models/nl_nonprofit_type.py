from __future__ import annotations

from .nonprofit_type import NonprofitType    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class NLNonprofitType(NonprofitType):
    """
NLNonprofitType: Non-profit organization type originating from the Netherlands.
    """
    class_: Literal['https://schema.org/NLNonprofitType'] = Field( # type: ignore
        default='https://schema.org/NLNonprofitType',
        alias='@type',
        serialization_alias='@type'
    )
