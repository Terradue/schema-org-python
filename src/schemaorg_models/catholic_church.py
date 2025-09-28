from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .church import Church

class CatholicChurch(Church):
    """
A Catholic church.
    """
    class_: Literal['https://schema.org/CatholicChurch'] = Field( # type: ignore
        default='https://schema.org/CatholicChurch',
        alias='@type',
        serialization_alias='@type'
    )
