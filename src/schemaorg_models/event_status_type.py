from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .status_enumeration import StatusEnumeration

class EventStatusType(StatusEnumeration):
    """
EventStatusType is an enumeration type whose instances represent several states that an Event may be in.
    """
    class_: Literal['https://schema.org/EventStatusType'] = Field( # type: ignore
        default='https://schema.org/EventStatusType',
        alias='@type',
        serialization_alias='@type'
    )
