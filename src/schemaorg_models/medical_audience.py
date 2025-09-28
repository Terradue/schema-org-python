from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .audience import Audience

class MedicalAudience(Audience):
    """
Medical audience for page.
    """
    class_: Literal['https://schema.org/MedicalAudience'] = Field( # type: ignore
        default='https://schema.org/MedicalAudience',
        alias='@type',
        serialization_alias='@type'
    )
