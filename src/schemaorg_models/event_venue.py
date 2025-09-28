from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .civic_structure import CivicStructure

class EventVenue(CivicStructure):
    """
An event venue.
    """
    class_: Literal['https://schema.org/EventVenue'] = Field( # type: ignore
        default='https://schema.org/EventVenue',
        alias='@type',
        serialization_alias='@type'
    )
