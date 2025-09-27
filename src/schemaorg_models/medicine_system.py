from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicineSystem(MedicalEnumeration):
    """
The system of medicine that includes this MedicalEntity, for example 'evidence-based', 'homeopathic', 'chiropractic', etc.
    """
    type_: Literal['https://schema.org/MedicineSystem'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicineSystem'),serialization_alias='class') # type: ignore
