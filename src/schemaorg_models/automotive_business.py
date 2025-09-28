from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class AutomotiveBusiness(LocalBusiness):
    """
Car repair, sales, or parts.
    """
    class_: Literal['https://schema.org/AutomotiveBusiness'] = Field( # type: ignore
        default='https://schema.org/AutomotiveBusiness',
        alias='@type',
        serialization_alias='@type'
    )
