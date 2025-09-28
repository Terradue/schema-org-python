from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .automotive_business import AutomotiveBusiness

class AutoRepair(AutomotiveBusiness):
    """
Car repair business.
    """
    class_: Literal['https://schema.org/AutoRepair'] = Field( # type: ignore
        default='https://schema.org/AutoRepair',
        alias='@type',
        serialization_alias='@type'
    )
