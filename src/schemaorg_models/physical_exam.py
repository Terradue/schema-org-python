from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class PhysicalExam(MedicalEnumeration):
    """
A type of physical examination of a patient performed by a physician. 
    """
    type_: Literal['https://schema.org/PhysicalExam'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PhysicalExam'),serialization_alias='class') # type: ignore
