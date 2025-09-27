from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class CertificationStatusEnumeration(Enumeration):
    """
Enumerates the different statuses of a Certification (Active and Inactive).
    """
    type_: Literal['https://schema.org/CertificationStatusEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CertificationStatusEnumeration'),serialization_alias='class') # type: ignore
