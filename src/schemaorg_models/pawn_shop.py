from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class PawnShop(Store):
    """
A shop that will buy, or lend money against the security of, personal possessions.
    """
    class_: Literal['https://schema.org/PawnShop'] = Field( # type: ignore
        default='https://schema.org/PawnShop',
        alias='@type',
        serialization_alias='@type'
    )
