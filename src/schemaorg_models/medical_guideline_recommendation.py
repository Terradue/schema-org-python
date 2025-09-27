from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_guideline import MedicalGuideline


class MedicalGuidelineRecommendation(MedicalGuideline):
    """
A guideline recommendation that is regarded as efficacious and where quality of the data supporting the recommendation is sound.
    """
    class_: Literal['https://schema.org/MedicalGuidelineRecommendation'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    recommendationStrength: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('recommendationStrength', 'https://schema.org/recommendationStrength'), serialization_alias='https://schema.org/recommendationStrength')
