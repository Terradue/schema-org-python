from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class RadioStation(LocalBusiness):
    """
A radio station.
    """
    class_: Literal['https://schema.org/RadioStation'] = Field( # type: ignore
        default='https://schema.org/RadioStation',
        alias='@type',
        serialization_alias='@type'
    )
