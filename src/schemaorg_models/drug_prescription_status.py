from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class DrugPrescriptionStatus(MedicalEnumeration):
    """
Indicates whether this drug is available by prescription or over-the-counter.
    """
    class_: Literal['https://schema.org/DrugPrescriptionStatus'] = Field(default='https://schema.org/DrugPrescriptionStatus', alias='class', serialization_alias='class') # type: ignore
