from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .local_business import LocalBusiness

class EmploymentAgency(LocalBusiness):
    """
An employment agency.
    """
    class_: Literal['https://schema.org/EmploymentAgency'] = Field( # type: ignore
        default='https://schema.org/EmploymentAgency',
        alias='@type',
        serialization_alias='@type'
    )
