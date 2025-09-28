from __future__ import annotations

from .quantity import Quantity    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Duration(Quantity):
    """
The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).
    """
    class_: Literal['https://schema.org/Duration'] = Field( # type: ignore
        default='https://schema.org/Duration',
        alias='@type',
        serialization_alias='@type'
    )
