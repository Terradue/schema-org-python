from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class AnimalShelter(LocalBusiness):
    """
Animal shelter.
    """
    class_: Literal['https://schema.org/AnimalShelter'] = Field( # type: ignore
        default='https://schema.org/AnimalShelter',
        alias='@type',
        serialization_alias='@type'
    )
