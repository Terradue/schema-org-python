from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .administrative_area import AdministrativeArea

class Country(AdministrativeArea):
    """
A country.
    """
    class_: Literal['https://schema.org/Country'] = Field( # type: ignore
        default='https://schema.org/Country',
        alias='@type',
        serialization_alias='@type'
    )
