from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AnimalShelter(LocalBusiness):
    """
Animal shelter.
    """
    class_: Literal['https://schema.org/AnimalShelter'] = Field( # type: ignore
        default='https://schema.org/AnimalShelter',
        alias='@type',
        serialization_alias='@type'
    )
