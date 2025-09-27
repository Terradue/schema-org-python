from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicineSystem(MedicalEnumeration):
    """
The system of medicine that includes this MedicalEntity, for example 'evidence-based', 'homeopathic', 'chiropractic', etc.
    """
    class_: Literal['https://schema.org/MedicineSystem'] = Field('class', alias='class', serialization_alias='class') # type: ignore
