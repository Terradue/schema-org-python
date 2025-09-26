from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.medical_condition import MedicalCondition


class MedicalSignOrSymptom(MedicalCondition):
    """
Any feature associated or not with a medical condition. In medicine a symptom is generally subjective while a sign is objective.
    """
    possibleTreatment: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = Field(default=None,validation_alias=AliasChoices('possibleTreatment', 'https://schema.org/possibleTreatment'),serialization_alias='https://schema.org/possibleTreatment')
