from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class AdultOrientedEnumeration(Enumeration):
    """
Enumeration of considerations that make a product relevant or potentially restricted for adults only.
    """
    class_: Literal['https://schema.org/AdultOrientedEnumeration'] = Field( # type: ignore
        default='https://schema.org/AdultOrientedEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
