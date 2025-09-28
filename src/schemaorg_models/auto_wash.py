from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .automotive_business import AutomotiveBusiness

class AutoWash(AutomotiveBusiness):
    """
A car wash business.
    """
    class_: Literal['https://schema.org/AutoWash'] = Field( # type: ignore
        default='https://schema.org/AutoWash',
        alias='@type',
        serialization_alias='@type'
    )
