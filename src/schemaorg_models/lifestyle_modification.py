from __future__ import annotations

from .medical_entity import MedicalEntity    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class LifestyleModification(MedicalEntity):
    """
A process of care involving exercise, changes to diet, fitness routines, and other lifestyle changes aimed at improving a health condition.
    """
    class_: Literal['https://schema.org/LifestyleModification'] = Field( # type: ignore
        default='https://schema.org/LifestyleModification',
        alias='@type',
        serialization_alias='@type'
    )
