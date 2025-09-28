from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .organization import Organization

class SearchRescueOrganization(Organization):
    """
A Search and Rescue organization of some kind.
    """
    class_: Literal['https://schema.org/SearchRescueOrganization'] = Field( # type: ignore
        default='https://schema.org/SearchRescueOrganization',
        alias='@type',
        serialization_alias='@type'
    )
