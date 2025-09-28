from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class LiquorStore(Store):
    """
A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.
    """
    class_: Literal['https://schema.org/LiquorStore'] = Field( # type: ignore
        default='https://schema.org/LiquorStore',
        alias='@type',
        serialization_alias='@type'
    )
