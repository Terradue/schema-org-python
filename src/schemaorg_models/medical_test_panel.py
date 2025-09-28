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
from .medical_test import MedicalTest

class MedicalTestPanel(MedicalTest):
    """
Any collection of tests commonly ordered together.
    """
    class_: Literal['https://schema.org/MedicalTestPanel'] = Field( # type: ignore
        default='https://schema.org/MedicalTestPanel',
        alias='@type',
        serialization_alias='@type'
    )
    subTest: Optional[Union["MedicalTest", List["MedicalTest"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subTest',
            'https://schema.org/subTest'
        ),
        serialization_alias='https://schema.org/subTest'
    )
