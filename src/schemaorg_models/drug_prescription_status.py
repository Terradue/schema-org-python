from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class DrugPrescriptionStatus(MedicalEnumeration):
    """
Indicates whether this drug is available by prescription or over-the-counter.
    """
    type_: Literal['https://schema.org/DrugPrescriptionStatus'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DrugPrescriptionStatus'),serialization_alias='class') # type: ignore
