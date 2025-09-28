from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ContactPointOption(Enumeration):
    """
Enumerated options related to a ContactPoint.
    """
    class_: Literal['https://schema.org/ContactPointOption'] = Field( # type: ignore
        default='https://schema.org/ContactPointOption',
        alias='@type',
        serialization_alias='@type'
    )
