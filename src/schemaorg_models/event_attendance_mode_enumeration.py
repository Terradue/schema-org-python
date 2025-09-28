from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class EventAttendanceModeEnumeration(Enumeration):
    """
An EventAttendanceModeEnumeration value is one of potentially several modes of organising an event, relating to whether it is online or offline.
    """
    class_: Literal['https://schema.org/EventAttendanceModeEnumeration'] = Field( # type: ignore
        default='https://schema.org/EventAttendanceModeEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
