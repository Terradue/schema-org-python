from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class HealthAspectEnumeration(Enumeration):
    """
HealthAspectEnumeration enumerates several aspects of health content online, each of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]].
    """
    class_: Literal['https://schema.org/HealthAspectEnumeration'] = Field( # type: ignore
        default='https://schema.org/HealthAspectEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
