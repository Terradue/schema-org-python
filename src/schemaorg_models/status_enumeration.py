from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class StatusEnumeration(Enumeration):
    """
Lists or enumerations dealing with status types.
    """
    class_: Literal['https://schema.org/StatusEnumeration'] = Field( # type: ignore
        default='https://schema.org/StatusEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
