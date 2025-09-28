from __future__ import annotations

from .organization import Organization    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PerformingGroup(Organization):
    """
A performance group, such as a band, an orchestra, or a circus.
    """
    class_: Literal['https://schema.org/PerformingGroup'] = Field( # type: ignore
        default='https://schema.org/PerformingGroup',
        alias='@type',
        serialization_alias='@type'
    )
