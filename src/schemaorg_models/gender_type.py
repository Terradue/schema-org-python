from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class GenderType(Enumeration):
    """
An enumeration of genders.
    """
    class_: Literal['https://schema.org/GenderType'] = Field( # type: ignore
        default='https://schema.org/GenderType',
        alias='@type',
        serialization_alias='@type'
    )
