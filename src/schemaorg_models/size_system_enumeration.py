from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .enumeration import Enumeration

class SizeSystemEnumeration(Enumeration):
    """
Enumerates common size systems for different categories of products, for example "EN-13402" or "UK" for wearables or "Imperial" for screws.
    """
    class_: Literal['https://schema.org/SizeSystemEnumeration'] = Field( # type: ignore
        default='https://schema.org/SizeSystemEnumeration',
        alias='@type',
        serialization_alias='@type'
    )
