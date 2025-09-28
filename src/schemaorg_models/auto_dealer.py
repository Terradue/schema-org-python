from __future__ import annotations

from .automotive_business import AutomotiveBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AutoDealer(AutomotiveBusiness):
    """
An car dealership.
    """
    class_: Literal['https://schema.org/AutoDealer'] = Field( # type: ignore
        default='https://schema.org/AutoDealer',
        alias='@type',
        serialization_alias='@type'
    )
