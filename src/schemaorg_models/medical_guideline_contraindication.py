from typing import Literal
from pydantic import Field
from schemaorg_models.medical_guideline import MedicalGuideline


class MedicalGuidelineContraindication(MedicalGuideline):
    """
A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound.
    """
    class_: Literal['https://schema.org/MedicalGuidelineContraindication'] = Field('class', alias='class', serialization_alias='class') # type: ignore
