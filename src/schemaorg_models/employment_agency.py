from __future__ import annotations

from .local_business import LocalBusiness    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class EmploymentAgency(LocalBusiness):
    """
An employment agency.
    """
    class_: Literal['https://schema.org/EmploymentAgency'] = Field( # type: ignore
        default='https://schema.org/EmploymentAgency',
        alias='@type',
        serialization_alias='@type'
    )
