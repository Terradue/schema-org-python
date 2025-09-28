from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class RestrictedDiet(Enumeration):
    """
A diet restricted to certain foods or preparations for cultural, religious, health or lifestyle reasons. 
    """
    class_: Literal['https://schema.org/RestrictedDiet'] = Field( # type: ignore
        default='https://schema.org/RestrictedDiet',
        alias='@type',
        serialization_alias='@type'
    )
