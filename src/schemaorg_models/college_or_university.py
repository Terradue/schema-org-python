from __future__ import annotations

from .educational_organization import EducationalOrganization    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class CollegeOrUniversity(EducationalOrganization):
    """
A college, university, or other third-level educational institution.
    """
    class_: Literal['https://schema.org/CollegeOrUniversity'] = Field( # type: ignore
        default='https://schema.org/CollegeOrUniversity',
        alias='@type',
        serialization_alias='@type'
    )
