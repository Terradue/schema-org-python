from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalStudyStatus(MedicalEnumeration):
    """
The status of a medical study. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalStudyStatus'] = Field(default='https://schema.org/MedicalStudyStatus', alias='class', serialization_alias='class') # type: ignore
