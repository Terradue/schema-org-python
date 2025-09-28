from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class MusicStore(Store):
    """
A music store.
    """
    class_: Literal['https://schema.org/MusicStore'] = Field( # type: ignore
        default='https://schema.org/MusicStore',
        alias='@type',
        serialization_alias='@type'
    )
