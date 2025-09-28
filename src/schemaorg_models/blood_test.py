from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_test import MedicalTest

class BloodTest(MedicalTest):
    """
A medical test performed on a sample of a patient's blood.
    """
    class_: Literal['https://schema.org/BloodTest'] = Field( # type: ignore
        default='https://schema.org/BloodTest',
        alias='@type',
        serialization_alias='@type'
    )
