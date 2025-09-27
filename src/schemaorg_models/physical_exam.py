from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class PhysicalExam(MedicalEnumeration):
    """
A type of physical examination of a patient performed by a physician. 
    """
    class_: Literal['https://schema.org/PhysicalExam'] = Field(default='https://schema.org/PhysicalExam', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
