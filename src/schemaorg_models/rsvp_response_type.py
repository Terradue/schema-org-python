from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class RsvpResponseType(Enumeration):
    """
RsvpResponseType is an enumeration type whose instances represent responding to an RSVP request.
    """
    class_: Literal['https://schema.org/RsvpResponseType'] = Field(default='https://schema.org/RsvpResponseType', alias='class', serialization_alias='class') # type: ignore
