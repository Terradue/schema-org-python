from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class TelevisionStation(LocalBusiness):
    """
A television station.
    """
    class_: Literal['https://schema.org/TelevisionStation'] = Field( # type: ignore
        default='https://schema.org/TelevisionStation',
        alias='@type',
        serialization_alias='@type'
    )
