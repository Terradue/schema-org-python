from __future__ import annotations

from .status_enumeration import StatusEnumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class LegalForceStatus(StatusEnumeration):
    """
A list of possible statuses for the legal force of a legislation.
    """
    class_: Literal['https://schema.org/LegalForceStatus'] = Field( # type: ignore
        default='https://schema.org/LegalForceStatus',
        alias='@type',
        serialization_alias='@type'
    )
