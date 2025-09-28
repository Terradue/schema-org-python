from __future__ import annotations

from .medical_entity import MedicalEntity    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MedicalIntangible(MedicalEntity):
    """
A utility class that serves as the umbrella for a number of 'intangible' things in the medical space.
    """
    class_: Literal['https://schema.org/MedicalIntangible'] = Field( # type: ignore
        default='https://schema.org/MedicalIntangible',
        alias='@type',
        serialization_alias='@type'
    )
