from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalStudyStatus(MedicalEnumeration):
    """
The status of a medical study. Enumerated type.
    """
    type_: Literal['https://schema.org/MedicalStudyStatus'] = Field(default='https://schema.org/MedicalStudyStatus', alias='@type', serialization_alias='@type') # type: ignore
