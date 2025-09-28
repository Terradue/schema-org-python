from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .service import Service

class Taxi(Service):
    """
A taxi.
    """
    class_: Literal['https://schema.org/Taxi'] = Field( # type: ignore
        default='https://schema.org/Taxi',
        alias='@type',
        serialization_alias='@type'
    )
