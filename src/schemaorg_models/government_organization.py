from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .organization import Organization

class GovernmentOrganization(Organization):
    """
A governmental organization or agency.
    """
    class_: Literal['https://schema.org/GovernmentOrganization'] = Field( # type: ignore
        default='https://schema.org/GovernmentOrganization',
        alias='@type',
        serialization_alias='@type'
    )
