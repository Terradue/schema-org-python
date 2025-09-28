from __future__ import annotations

from .landform import Landform    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Volcano(Landform):
    """
A volcano, like Fujisan.
    """
    class_: Literal['https://schema.org/Volcano'] = Field( # type: ignore
        default='https://schema.org/Volcano',
        alias='@type',
        serialization_alias='@type'
    )
