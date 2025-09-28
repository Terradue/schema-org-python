from __future__ import annotations

from .church import Church    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class CatholicChurch(Church):
    """
A Catholic church.
    """
    class_: Literal['https://schema.org/CatholicChurch'] = Field( # type: ignore
        default='https://schema.org/CatholicChurch',
        alias='@type',
        serialization_alias='@type'
    )
