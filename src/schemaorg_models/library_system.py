from __future__ import annotations

from .organization import Organization    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class LibrarySystem(Organization):
    """
A [[LibrarySystem]] is a collaborative system amongst several libraries.
    """
    class_: Literal['https://schema.org/LibrarySystem'] = Field( # type: ignore
        default='https://schema.org/LibrarySystem',
        alias='@type',
        serialization_alias='@type'
    )
