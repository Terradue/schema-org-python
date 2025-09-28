from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class CertificationStatusEnumeration(Enumeration):
    """
Enumerates the different statuses of a Certification (Active and Inactive).
    """
    class_: Literal['https://schema.org/CertificationStatusEnumeration'] = Field( # type: ignore
        default='https://schema.org/CertificationStatusEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
