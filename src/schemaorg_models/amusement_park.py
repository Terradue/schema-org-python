from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .entertainment_business import EntertainmentBusiness

class AmusementPark(EntertainmentBusiness):
    """
An amusement park.
    """
    class_: Literal['https://schema.org/AmusementPark'] = Field( # type: ignore
        default='https://schema.org/AmusementPark',
        alias='@type',
        serialization_alias='@type'
    )
