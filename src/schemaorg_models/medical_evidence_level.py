from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalEvidenceLevel(MedicalEnumeration):
    """
Level of evidence for a medical guideline. Enumerated type.
    """
    type_: Literal['https://schema.org/MedicalEvidenceLevel'] = Field(default='https://schema.org/MedicalEvidenceLevel', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
