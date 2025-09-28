from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class TierBenefitEnumeration(Enumeration):
    """
An enumeration of possible benefits as part of a loyalty (members) program.
    """
    class_: Literal['https://schema.org/TierBenefitEnumeration'] = Field( # type: ignore
        default='https://schema.org/TierBenefitEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
