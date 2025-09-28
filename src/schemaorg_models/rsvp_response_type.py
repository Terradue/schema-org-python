from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.enumeration import Enumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class RsvpResponseType(Enumeration):
    """
RsvpResponseType is an enumeration type whose instances represent responding to an RSVP request.
    """
    class_: Literal['https://schema.org/RsvpResponseType'] = Field( # type: ignore
        default='https://schema.org/RsvpResponseType',
        alias='@type',
        serialization_alias='@type'
    )
