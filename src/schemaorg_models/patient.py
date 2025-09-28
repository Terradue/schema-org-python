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
from .medical_condition import MedicalCondition
from .medical_audience import MedicalAudience
from .drug import Drug

class Patient(MedicalAudience):
    """
A patient is any person recipient of health care services.
    """
    class_: Literal['https://schema.org/Patient'] = Field( # type: ignore
        default='https://schema.org/Patient',
        alias='@type',
        serialization_alias='@type'
    )
    healthCondition: Optional[Union[MedicalCondition, List[MedicalCondition]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'healthCondition',
            'https://schema.org/healthCondition'
        ),
        serialization_alias='https://schema.org/healthCondition'
    )
    diagnosis: Optional[Union[MedicalCondition, List[MedicalCondition]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'diagnosis',
            'https://schema.org/diagnosis'
        ),
        serialization_alias='https://schema.org/diagnosis'
    )
    drug: Optional[Union[Drug, List[Drug]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'drug',
            'https://schema.org/drug'
        ),
        serialization_alias='https://schema.org/drug'
    )
