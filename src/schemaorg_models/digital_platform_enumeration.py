from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DigitalPlatformEnumeration(Enumeration):
    """
Enumerates some common technology platforms, for use with properties such as [[actionPlatform]]. It is not supposed to be comprehensive - when a suitable code is not enumerated here, textual or URL values can be used instead. These codes are at a fairly high level and do not deal with versioning and other nuance. Additional codes can be suggested [in github](https://github.com/schemaorg/schemaorg/issues/3057). 
    """
    class_: Literal['https://schema.org/DigitalPlatformEnumeration'] = Field( # type: ignore
        default='https://schema.org/DigitalPlatformEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
