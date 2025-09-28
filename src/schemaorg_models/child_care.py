from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ChildCare(LocalBusiness):
    """
A Childcare center.
    """
    class_: Literal['https://schema.org/ChildCare'] = Field( # type: ignore
        default='https://schema.org/ChildCare',
        alias='@type',
        serialization_alias='@type'
    )
