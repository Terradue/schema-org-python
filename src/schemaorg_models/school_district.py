from __future__ import annotations

from .administrative_area import AdministrativeArea    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SchoolDistrict(AdministrativeArea):
    """
A School District is an administrative area for the administration of schools.
    """
    class_: Literal['https://schema.org/SchoolDistrict'] = Field( # type: ignore
        default='https://schema.org/SchoolDistrict',
        alias='@type',
        serialization_alias='@type'
    )
