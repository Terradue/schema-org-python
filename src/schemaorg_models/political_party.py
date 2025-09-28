from __future__ import annotations

from .organization import Organization    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PoliticalParty(Organization):
    """
Organization: Political Party.
    """
    class_: Literal['https://schema.org/PoliticalParty'] = Field( # type: ignore
        default='https://schema.org/PoliticalParty',
        alias='@type',
        serialization_alias='@type'
    )
