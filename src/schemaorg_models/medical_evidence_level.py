from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalEvidenceLevel(MedicalEnumeration):
    """
Level of evidence for a medical guideline. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalEvidenceLevel'] = Field('class', alias='class', serialization_alias='class') # type: ignore
