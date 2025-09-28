from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class Library(LocalBusiness):
    """
A library.
    """
    class_: Literal['https://schema.org/Library'] = Field( # type: ignore
        default='https://schema.org/Library',
        alias='@type',
        serialization_alias='@type'
    )
