from __future__ import annotations

from .administrative_area import AdministrativeArea    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class City(AdministrativeArea):
    """
A city or town.
    """
    class_: Literal['https://schema.org/City'] = Field( # type: ignore
        default='https://schema.org/City',
        alias='@type',
        serialization_alias='@type'
    )
