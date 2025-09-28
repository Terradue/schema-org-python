from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PhysicalActivityCategory(Enumeration):
    """
Categories of physical activity, organized by physiologic classification.
    """
    class_: Literal['https://schema.org/PhysicalActivityCategory'] = Field( # type: ignore
        default='https://schema.org/PhysicalActivityCategory',
        alias='@type',
        serialization_alias='@type'
    )
