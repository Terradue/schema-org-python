from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class RecyclingCenter(LocalBusiness):
    """
A recycling center.
    """
    class_: Literal['https://schema.org/RecyclingCenter'] = Field( # type: ignore
        default='https://schema.org/RecyclingCenter',
        alias='@type',
        serialization_alias='@type'
    )
