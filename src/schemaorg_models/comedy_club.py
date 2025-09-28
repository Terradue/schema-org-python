from __future__ import annotations

from .entertainment_business import EntertainmentBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ComedyClub(EntertainmentBusiness):
    """
A comedy club.
    """
    class_: Literal['https://schema.org/ComedyClub'] = Field( # type: ignore
        default='https://schema.org/ComedyClub',
        alias='@type',
        serialization_alias='@type'
    )
