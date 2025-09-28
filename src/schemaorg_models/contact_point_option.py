from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class ContactPointOption(Enumeration):
    """
Enumerated options related to a ContactPoint.
    """
    class_: Literal['https://schema.org/ContactPointOption'] = Field( # type: ignore
        default='https://schema.org/ContactPointOption',
        alias='@type',
        serialization_alias='@type'
    )
