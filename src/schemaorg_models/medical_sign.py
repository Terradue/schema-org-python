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
from .medical_sign_or_symptom import MedicalSignOrSymptom
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_test import MedicalTest
    from .physical_exam import PhysicalExam

class MedicalSign(MedicalSignOrSymptom):
    """
Any physical manifestation of a person's medical condition discoverable by objective diagnostic tests or physical examination.
    """
    class_: Literal['https://schema.org/MedicalSign'] = Field( # type: ignore
        default='https://schema.org/MedicalSign',
        alias='@type',
        serialization_alias='@type'
    )
    identifyingTest: Optional[Union["MedicalTest", List["MedicalTest"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'identifyingTest',
            'https://schema.org/identifyingTest'
        ),
        serialization_alias='https://schema.org/identifyingTest'
    )
    identifyingExam: Optional[Union["PhysicalExam", List["PhysicalExam"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'identifyingExam',
            'https://schema.org/identifyingExam'
        ),
        serialization_alias='https://schema.org/identifyingExam'
    )
