from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalObservationalStudyDesign(MedicalEnumeration):
    """
Design models for observational medical studies. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalObservationalStudyDesign'] = Field(default='https://schema.org/MedicalObservationalStudyDesign', alias='@type', serialization_alias='@type') # type: ignore
