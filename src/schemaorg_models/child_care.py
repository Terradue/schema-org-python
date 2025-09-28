from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class ChildCare(LocalBusiness):
    """
A Childcare center.
    """
    class_: Literal['https://schema.org/ChildCare'] = Field( # type: ignore
        default='https://schema.org/ChildCare',
        alias='@type',
        serialization_alias='@type'
    )
