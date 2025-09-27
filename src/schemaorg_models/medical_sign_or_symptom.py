from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_condition import MedicalCondition


class MedicalSignOrSymptom(MedicalCondition):
    """
Any feature associated or not with a medical condition. In medicine a symptom is generally subjective while a sign is objective.
    """
    type_: Literal['https://schema.org/MedicalSignOrSymptom'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalSignOrSymptom'),serialization_alias='class') # type: ignore
    possibleTreatment: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = Field(default=None,validation_alias=AliasChoices('possibleTreatment', 'https://schema.org/possibleTreatment'),serialization_alias='https://schema.org/possibleTreatment')
