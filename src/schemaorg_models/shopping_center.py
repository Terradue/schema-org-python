from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ShoppingCenter(LocalBusiness):
    """
A shopping center or mall.
    """
    class_: Literal['https://schema.org/ShoppingCenter'] = Field( # type: ignore
        default='https://schema.org/ShoppingCenter',
        alias='@type',
        serialization_alias='@type'
    )
