from typing import Literal
from pydantic import Field
from schemaorg_models.status_enumeration import StatusEnumeration


class LegalForceStatus(StatusEnumeration):
    """
A list of possible statuses for the legal force of a legislation.
    """
    class_: Literal['https://schema.org/LegalForceStatus'] = Field(default='https://schema.org/LegalForceStatus', alias='@type', serialization_alias='@type') # type: ignore
