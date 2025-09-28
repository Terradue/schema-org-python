from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DigitalDocumentPermissionType(Enumeration):
    """
A type of permission which can be granted for accessing a digital document.
    """
    class_: Literal['https://schema.org/DigitalDocumentPermissionType'] = Field( # type: ignore
        default='https://schema.org/DigitalDocumentPermissionType',
        alias='@type',
        serialization_alias='@type'
    )
