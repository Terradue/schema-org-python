from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalTrialDesign(MedicalEnumeration):
    """
Design models for medical trials. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalTrialDesign'] = Field(default='https://schema.org/MedicalTrialDesign', alias='@type', serialization_alias='@type') # type: ignore
