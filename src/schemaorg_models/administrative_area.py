from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .place import Place

class AdministrativeArea(Place):
    """
A geographical region, typically under the jurisdiction of a particular government.
    """
    class_: Literal['https://schema.org/AdministrativeArea'] = Field( # type: ignore
        default='https://schema.org/AdministrativeArea',
        alias='@type',
        serialization_alias='@type'
    )
