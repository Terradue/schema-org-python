from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class RsvpResponseType(Enumeration):
    """
RsvpResponseType is an enumeration type whose instances represent responding to an RSVP request.
    """
    type_: Literal['https://schema.org/RsvpResponseType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RsvpResponseType'),serialization_alias='class') # type: ignore
