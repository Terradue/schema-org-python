from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AutomotiveBusiness(LocalBusiness):
    """
Car repair, sales, or parts.
    """
    class_: Literal['https://schema.org/AutomotiveBusiness'] = Field( # type: ignore
        default='https://schema.org/AutomotiveBusiness',
        alias='@type',
        serialization_alias='@type'
    )
