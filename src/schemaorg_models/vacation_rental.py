from __future__ import annotations

from .lodging_business import LodgingBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class VacationRental(LodgingBusiness):
    """
A kind of lodging business that focuses on renting single properties for limited time.
    """
    class_: Literal['https://schema.org/VacationRental'] = Field( # type: ignore
        default='https://schema.org/VacationRental',
        alias='@type',
        serialization_alias='@type'
    )
