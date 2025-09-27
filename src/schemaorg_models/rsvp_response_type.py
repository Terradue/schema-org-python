from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class RsvpResponseType(Enumeration):
    """
RsvpResponseType is an enumeration type whose instances represent responding to an RSVP request.
    """
    class_: Literal['https://schema.org/RsvpResponseType'] = Field(default='https://schema.org/RsvpResponseType', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
