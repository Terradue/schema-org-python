from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Library(LocalBusiness):
    """
A library.
    """
    class_: Literal['https://schema.org/Library'] = Field( # type: ignore
        default='https://schema.org/Library',
        alias='@type',
        serialization_alias='@type'
    )
