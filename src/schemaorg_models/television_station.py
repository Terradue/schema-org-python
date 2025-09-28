from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class TelevisionStation(LocalBusiness):
    """
A television station.
    """
    class_: Literal['https://schema.org/TelevisionStation'] = Field( # type: ignore
        default='https://schema.org/TelevisionStation',
        alias='@type',
        serialization_alias='@type'
    )
