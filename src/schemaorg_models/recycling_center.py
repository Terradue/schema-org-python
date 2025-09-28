from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class RecyclingCenter(LocalBusiness):
    """
A recycling center.
    """
    class_: Literal['https://schema.org/RecyclingCenter'] = Field( # type: ignore
        default='https://schema.org/RecyclingCenter',
        alias='@type',
        serialization_alias='@type'
    )
