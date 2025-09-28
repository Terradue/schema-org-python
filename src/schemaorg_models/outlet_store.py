from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class OutletStore(Store):
    """
An outlet store.
    """
    class_: Literal['https://schema.org/OutletStore'] = Field( # type: ignore
        default='https://schema.org/OutletStore',
        alias='@type',
        serialization_alias='@type'
    )
