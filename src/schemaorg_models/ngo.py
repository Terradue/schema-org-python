from __future__ import annotations

from .organization import Organization    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class NGO(Organization):
    """
Organization: Non-governmental Organization.
    """
    class_: Literal['https://schema.org/NGO'] = Field( # type: ignore
        default='https://schema.org/NGO',
        alias='@type',
        serialization_alias='@type'
    )
