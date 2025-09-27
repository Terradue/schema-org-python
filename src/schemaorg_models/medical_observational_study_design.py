from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalObservationalStudyDesign(MedicalEnumeration):
    """
Design models for observational medical studies. Enumerated type.
    """
    type_: Literal['https://schema.org/MedicalObservationalStudyDesign'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalObservationalStudyDesign'),serialization_alias='class') # type: ignore
