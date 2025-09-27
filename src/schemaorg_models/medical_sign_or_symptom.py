from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_condition import MedicalCondition


class MedicalSignOrSymptom(MedicalCondition):
    """
Any feature associated or not with a medical condition. In medicine a symptom is generally subjective while a sign is objective.
    """
    class_: Literal['https://schema.org/MedicalSignOrSymptom'] = Field(default='https://schema.org/MedicalSignOrSymptom', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    possibleTreatment: Optional[Union["MedicalTherapy", List["MedicalTherapy"]]] = Field(default=None, validation_alias=AliasChoices('possibleTreatment', 'https://schema.org/possibleTreatment'), serialization_alias='https://schema.org/possibleTreatment')
