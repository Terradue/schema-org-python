from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class ComputerStore(Store):
    """
A computer store.
    """
    class_: Literal['https://schema.org/ComputerStore'] = Field( # type: ignore
        default='https://schema.org/ComputerStore',
        alias='@type',
        serialization_alias='@type'
    )
