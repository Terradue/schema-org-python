from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class CertificationStatusEnumeration(Enumeration):
    """
Enumerates the different statuses of a Certification (Active and Inactive).
    """
    class_: Literal['https://schema.org/CertificationStatusEnumeration'] = Field(default='https://schema.org/CertificationStatusEnumeration', alias='@type', serialization_alias='@type') # type: ignore
