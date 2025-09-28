from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .qualitative_value import QualitativeValue

class BedType(QualitativeValue):
    """
A type of bed. This is used for indicating the bed or beds available in an accommodation.
    """
    class_: Literal['https://schema.org/BedType'] = Field( # type: ignore
        default='https://schema.org/BedType',
        alias='@type',
        serialization_alias='@type'
    )
