from __future__ import annotations

from .store import Store    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class OutletStore(Store):
    """
An outlet store.
    """
    class_: Literal['https://schema.org/OutletStore'] = Field( # type: ignore
        default='https://schema.org/OutletStore',
        alias='@type',
        serialization_alias='@type'
    )
