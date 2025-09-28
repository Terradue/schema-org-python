from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .organization import Organization

class Consortium(Organization):
    """
A Consortium is a membership [[Organization]] whose members are typically Organizations.
    """
    class_: Literal['https://schema.org/Consortium'] = Field( # type: ignore
        default='https://schema.org/Consortium',
        alias='@type',
        serialization_alias='@type'
    )
