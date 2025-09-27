from typing import Literal
from pydantic import Field
from schemaorg_models.medical_guideline import MedicalGuideline


class MedicalGuidelineContraindication(MedicalGuideline):
    """
A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound.
    """
    type_: Literal['https://schema.org/MedicalGuidelineContraindication'] = Field(default='https://schema.org/MedicalGuidelineContraindication', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
