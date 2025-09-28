from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .automotive_business import AutomotiveBusiness

class AutoBodyShop(AutomotiveBusiness):
    """
Auto body shop.
    """
    class_: Literal['https://schema.org/AutoBodyShop'] = Field( # type: ignore
        default='https://schema.org/AutoBodyShop',
        alias='@type',
        serialization_alias='@type'
    )
