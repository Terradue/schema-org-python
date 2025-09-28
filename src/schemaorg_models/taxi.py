from __future__ import annotations

from .service import Service    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Taxi(Service):
    """
A taxi.
    """
    class_: Literal['https://schema.org/Taxi'] = Field( # type: ignore
        default='https://schema.org/Taxi',
        alias='@type',
        serialization_alias='@type'
    )
