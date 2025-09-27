from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_sign_or_symptom import MedicalSignOrSymptom

from schemaorg_models.medical_test import MedicalTest
from schemaorg_models.physical_exam import PhysicalExam

class MedicalSign(MedicalSignOrSymptom):
    """
Any physical manifestation of a person's medical condition discoverable by objective diagnostic tests or physical examination.
    """
    type_: Literal['https://schema.org/MedicalSign'] = Field(default='https://schema.org/MedicalSign', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    identifyingTest: Optional[Union[MedicalTest, List[MedicalTest]]] = Field(default=None, validation_alias=AliasChoices('identifyingTest', 'https://schema.org/identifyingTest'), serialization_alias='https://schema.org/identifyingTest')
    identifyingExam: Optional[Union[PhysicalExam, List[PhysicalExam]]] = Field(default=None, validation_alias=AliasChoices('identifyingExam', 'https://schema.org/identifyingExam'), serialization_alias='https://schema.org/identifyingExam')
