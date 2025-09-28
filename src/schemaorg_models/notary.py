from __future__ import annotations

from .legal_service import LegalService    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Notary(LegalService):
    """
A notary.
    """
    class_: Literal['https://schema.org/Notary'] = Field( # type: ignore
        default='https://schema.org/Notary',
        alias='@type',
        serialization_alias='@type'
    )
