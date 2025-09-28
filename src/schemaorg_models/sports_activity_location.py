from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class SportsActivityLocation(LocalBusiness):
    """
A sub property of location. The sports activity location where this action occurred.
    """
    class_: Literal['https://schema.org/SportsActivityLocation'] = Field( # type: ignore
        default='https://schema.org/SportsActivityLocation',
        alias='@type',
        serialization_alias='@type'
    )
