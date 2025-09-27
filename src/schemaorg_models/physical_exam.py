from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class PhysicalExam(MedicalEnumeration):
    """
A type of physical examination of a patient performed by a physician. 
    """
    class_: Literal['https://schema.org/PhysicalExam'] = Field(default='https://schema.org/PhysicalExam', alias='class', serialization_alias='class') # type: ignore
