from __future__ import annotations

from .physician import Physician    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PhysiciansOffice(Physician):
    """
A doctor's office or clinic.
    """
    class_: Literal['https://schema.org/PhysiciansOffice'] = Field( # type: ignore
        default='https://schema.org/PhysiciansOffice',
        alias='@type',
        serialization_alias='@type'
    )
