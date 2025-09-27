from typing import Literal
from pydantic import Field
from schemaorg_models.medical_sign_or_symptom import MedicalSignOrSymptom


class MedicalSymptom(MedicalSignOrSymptom):
    """
Any complaint sensed and expressed by the patient (therefore defined as subjective)  like stomachache, lower-back pain, or fatigue.
    """
    type_: Literal['https://schema.org/MedicalSymptom'] = Field(default='https://schema.org/MedicalSymptom', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
