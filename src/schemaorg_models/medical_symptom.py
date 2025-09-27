from typing import Literal
from pydantic import Field
from schemaorg_models.medical_sign_or_symptom import MedicalSignOrSymptom


class MedicalSymptom(MedicalSignOrSymptom):
    """
Any complaint sensed and expressed by the patient (therefore defined as subjective)  like stomachache, lower-back pain, or fatigue.
    """
    class_: Literal['https://schema.org/MedicalSymptom'] = Field('class', alias='class', serialization_alias='class') # type: ignore
