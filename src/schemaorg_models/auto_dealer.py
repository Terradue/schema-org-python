from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .automotive_business import AutomotiveBusiness

class AutoDealer(AutomotiveBusiness):
    """
An car dealership.
    """
    class_: Literal['https://schema.org/AutoDealer'] = Field( # type: ignore
        default='https://schema.org/AutoDealer',
        alias='@type',
        serialization_alias='@type'
    )
