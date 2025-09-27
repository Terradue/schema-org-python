from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_sign_or_symptom import MedicalSignOrSymptom


class MedicalSymptom(MedicalSignOrSymptom):
    """
Any complaint sensed and expressed by the patient (therefore defined as subjective)  like stomachache, lower-back pain, or fatigue.
    """
    type_: Literal['https://schema.org/MedicalSymptom'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalSymptom'),serialization_alias='class') # type: ignore
