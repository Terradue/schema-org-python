from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class Store(LocalBusiness):
    """
A retail good store.
    """
    class_: Literal['https://schema.org/Store'] = Field( # type: ignore
        default='https://schema.org/Store',
        alias='@type',
        serialization_alias='@type'
    )
