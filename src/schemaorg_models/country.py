from __future__ import annotations

from .administrative_area import AdministrativeArea    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Country(AdministrativeArea):
    """
A country.
    """
    class_: Literal['https://schema.org/Country'] = Field( # type: ignore
        default='https://schema.org/Country',
        alias='@type',
        serialization_alias='@type'
    )
