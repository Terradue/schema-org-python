from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class DrugPrescriptionStatus(MedicalEnumeration):
    """
Indicates whether this drug is available by prescription or over-the-counter.
    """
    class_: Literal['https://schema.org/DrugPrescriptionStatus'] = Field(default='https://schema.org/DrugPrescriptionStatus', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
