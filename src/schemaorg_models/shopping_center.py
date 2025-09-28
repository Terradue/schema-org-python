from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class ShoppingCenter(LocalBusiness):
    """
A shopping center or mall.
    """
    class_: Literal['https://schema.org/ShoppingCenter'] = Field( # type: ignore
        default='https://schema.org/ShoppingCenter',
        alias='@type',
        serialization_alias='@type'
    )
