from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .entertainment_business import EntertainmentBusiness

class NightClub(EntertainmentBusiness):
    """
A nightclub or discotheque.
    """
    class_: Literal['https://schema.org/NightClub'] = Field( # type: ignore
        default='https://schema.org/NightClub',
        alias='@type',
        serialization_alias='@type'
    )
