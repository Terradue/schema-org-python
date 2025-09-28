from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .status_enumeration import StatusEnumeration

class LegalForceStatus(StatusEnumeration):
    """
A list of possible statuses for the legal force of a legislation.
    """
    class_: Literal['https://schema.org/LegalForceStatus'] = Field( # type: ignore
        default='https://schema.org/LegalForceStatus',
        alias='@type',
        serialization_alias='@type'
    )
