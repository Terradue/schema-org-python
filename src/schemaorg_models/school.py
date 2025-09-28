from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .educational_organization import EducationalOrganization

class School(EducationalOrganization):
    """
A school.
    """
    class_: Literal['https://schema.org/School'] = Field( # type: ignore
        default='https://schema.org/School',
        alias='@type',
        serialization_alias='@type'
    )
