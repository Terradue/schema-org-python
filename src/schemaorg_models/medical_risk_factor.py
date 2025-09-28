from __future__ import annotations
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
from .medical_entity import MedicalEntity

class MedicalRiskFactor(MedicalEntity):
    """
A risk factor is anything that increases a person's likelihood of developing or contracting a disease, medical condition, or complication.
    """
    class_: Literal['https://schema.org/MedicalRiskFactor'] = Field( # type: ignore
        default='https://schema.org/MedicalRiskFactor',
        alias='@type',
        serialization_alias='@type'
    )
    increasesRiskOf: Optional[Union["MedicalEntity", List["MedicalEntity"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'increasesRiskOf',
            'https://schema.org/increasesRiskOf'
        ),
        serialization_alias='https://schema.org/increasesRiskOf'
    )
