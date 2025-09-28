from __future__ import annotations

from .medical_guideline import MedicalGuideline    

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)

class MedicalGuidelineRecommendation(MedicalGuideline):
    """
A guideline recommendation that is regarded as efficacious and where quality of the data supporting the recommendation is sound.
    """
    class_: Literal['https://schema.org/MedicalGuidelineRecommendation'] = Field( # type: ignore
        default='https://schema.org/MedicalGuidelineRecommendation',
        alias='@type',
        serialization_alias='@type'
    )
    recommendationStrength: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recommendationStrength',
            'https://schema.org/recommendationStrength'
        ),
        serialization_alias='https://schema.org/recommendationStrength'
    )
