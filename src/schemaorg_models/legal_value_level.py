from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class LegalValueLevel(Enumeration):
    """
A list of possible levels for the legal validity of a legislation.
    """
    class_: Literal['https://schema.org/LegalValueLevel'] = Field( # type: ignore
        default='https://schema.org/LegalValueLevel',
        alias='@type',
        serialization_alias='@type'
    )
