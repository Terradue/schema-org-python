from __future__ import annotations

from .store import Store    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class LiquorStore(Store):
    """
A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.
    """
    class_: Literal['https://schema.org/LiquorStore'] = Field( # type: ignore
        default='https://schema.org/LiquorStore',
        alias='@type',
        serialization_alias='@type'
    )
