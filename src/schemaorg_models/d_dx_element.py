from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_intangible import MedicalIntangible

from schemaorg_models.medical_sign_or_symptom import MedicalSignOrSymptom
from schemaorg_models.medical_condition import MedicalCondition

class DDxElement(MedicalIntangible):
    """
An alternative, closely-related condition typically considered later in the differential diagnosis process along with the signs that are used to distinguish it.
    """
    type_: Literal['https://schema.org/DDxElement'] = Field(default='https://schema.org/DDxElement', alias='@type', serialization_alias='@type') # type: ignore
    distinguishingSign: Optional[Union[MedicalSignOrSymptom, List[MedicalSignOrSymptom]]] = Field(default=None, validation_alias=AliasChoices('distinguishingSign', 'https://schema.org/distinguishingSign'), serialization_alias='https://schema.org/distinguishingSign')
    diagnosis: Optional[Union[MedicalCondition, List[MedicalCondition]]] = Field(default=None, validation_alias=AliasChoices('diagnosis', 'https://schema.org/diagnosis'), serialization_alias='https://schema.org/diagnosis')
