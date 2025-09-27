from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class CertificationStatusEnumeration(Enumeration):
    """
Enumerates the different statuses of a Certification (Active and Inactive).
    """
    class_: Literal['https://schema.org/CertificationStatusEnumeration'] = Field('class', alias='class', serialization_alias='class') # type: ignore
