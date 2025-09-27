from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalEvidenceLevel(MedicalEnumeration):
    """
Level of evidence for a medical guideline. Enumerated type.
    """
    type_: Literal['https://schema.org/MedicalEvidenceLevel'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalEvidenceLevel'),serialization_alias='class') # type: ignore
