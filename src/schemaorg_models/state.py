from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .administrative_area import AdministrativeArea

class State(AdministrativeArea):
    """
A state or province of a country.
    """
    class_: Literal['https://schema.org/State'] = Field( # type: ignore
        default='https://schema.org/State',
        alias='@type',
        serialization_alias='@type'
    )
