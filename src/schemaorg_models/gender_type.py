from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class GenderType(Enumeration):
    """
An enumeration of genders.
    """
    class_: Literal['https://schema.org/GenderType'] = Field( # type: ignore
        default='https://schema.org/GenderType',
        alias='@type',
        serialization_alias='@type'
    )
