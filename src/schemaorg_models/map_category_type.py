from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MapCategoryType(Enumeration):
    """
An enumeration of several kinds of Map.
    """
    class_: Literal['https://schema.org/MapCategoryType'] = Field( # type: ignore
        default='https://schema.org/MapCategoryType',
        alias='@type',
        serialization_alias='@type'
    )
