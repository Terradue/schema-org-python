from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalAudienceType(MedicalEnumeration):
    """
Target audiences types for medical web pages. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalAudienceType'] = Field(default='https://schema.org/MedicalAudienceType', alias='class', serialization_alias='class') # type: ignore
