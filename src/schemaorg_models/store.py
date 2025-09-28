from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Store(LocalBusiness):
    """
A retail good store.
    """
    class_: Literal['https://schema.org/Store'] = Field( # type: ignore
        default='https://schema.org/Store',
        alias='@type',
        serialization_alias='@type'
    )
