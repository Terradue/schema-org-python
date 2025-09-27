from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalTrialDesign(MedicalEnumeration):
    """
Design models for medical trials. Enumerated type.
    """
    type_: Literal['https://schema.org/MedicalTrialDesign'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalTrialDesign'),serialization_alias='class') # type: ignore
