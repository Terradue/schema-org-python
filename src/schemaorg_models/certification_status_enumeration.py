from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class CertificationStatusEnumeration(Enumeration):
    """
Enumerates the different statuses of a Certification (Active and Inactive).
    """
    class_: Literal['https://schema.org/CertificationStatusEnumeration'] = Field(default='https://schema.org/CertificationStatusEnumeration', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
