from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class RsvpResponseType(Enumeration):
    """
RsvpResponseType is an enumeration type whose instances represent responding to an RSVP request.
    """
    class_: Literal['https://schema.org/RsvpResponseType'] = Field( # type: ignore
        default='https://schema.org/RsvpResponseType',
        alias='@type',
        serialization_alias='@type'
    )
