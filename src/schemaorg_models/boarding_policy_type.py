from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BoardingPolicyType(Enumeration):
    """
A type of boarding policy used by an airline.
    """
    class_: Literal['https://schema.org/BoardingPolicyType'] = Field( # type: ignore
        default='https://schema.org/BoardingPolicyType',
        alias='@type',
        serialization_alias='@type'
    )
