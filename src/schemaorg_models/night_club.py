from __future__ import annotations

from .entertainment_business import EntertainmentBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class NightClub(EntertainmentBusiness):
    """
A nightclub or discotheque.
    """
    class_: Literal['https://schema.org/NightClub'] = Field( # type: ignore
        default='https://schema.org/NightClub',
        alias='@type',
        serialization_alias='@type'
    )
