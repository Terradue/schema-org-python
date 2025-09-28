from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class Specialty(Enumeration):
    """
One of the domain specialities to which this web page's content applies.
    """
    class_: Literal['https://schema.org/Specialty'] = Field( # type: ignore
        default='https://schema.org/Specialty',
        alias='@type',
        serialization_alias='@type'
    )
