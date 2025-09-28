from __future__ import annotations

from .health_and_beauty_business import HealthAndBeautyBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class TattooParlor(HealthAndBeautyBusiness):
    """
A tattoo parlor.
    """
    class_: Literal['https://schema.org/TattooParlor'] = Field( # type: ignore
        default='https://schema.org/TattooParlor',
        alias='@type',
        serialization_alias='@type'
    )
