from typing import Literal
from pydantic import Field
from schemaorg_models.status_enumeration import StatusEnumeration


class LegalForceStatus(StatusEnumeration):
    """
A list of possible statuses for the legal force of a legislation.
    """
    type_: Literal['https://schema.org/LegalForceStatus'] = Field(default='https://schema.org/LegalForceStatus', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
