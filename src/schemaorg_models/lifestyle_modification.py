from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .medical_entity import MedicalEntity

class LifestyleModification(MedicalEntity):
    """
A process of care involving exercise, changes to diet, fitness routines, and other lifestyle changes aimed at improving a health condition.
    """
    class_: Literal['https://schema.org/LifestyleModification'] = Field( # type: ignore
        default='https://schema.org/LifestyleModification',
        alias='@type',
        serialization_alias='@type'
    )
