from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .educational_organization import EducationalOrganization

class HighSchool(EducationalOrganization):
    """
A high school.
    """
    class_: Literal['https://schema.org/HighSchool'] = Field( # type: ignore
        default='https://schema.org/HighSchool',
        alias='@type',
        serialization_alias='@type'
    )
