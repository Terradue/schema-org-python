from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .administrative_area import AdministrativeArea

class City(AdministrativeArea):
    """
A city or town.
    """
    class_: Literal['https://schema.org/City'] = Field( # type: ignore
        default='https://schema.org/City',
        alias='@type',
        serialization_alias='@type'
    )
