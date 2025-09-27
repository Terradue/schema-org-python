from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.status_enumeration import StatusEnumeration


class LegalForceStatus(StatusEnumeration):
    """
A list of possible statuses for the legal force of a legislation.
    """
    type_: Literal['https://schema.org/LegalForceStatus'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/LegalForceStatus'),serialization_alias='class') # type: ignore
