from __future__ import annotations

from .educational_organization import EducationalOrganization    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class School(EducationalOrganization):
    """
A school.
    """
    class_: Literal['https://schema.org/School'] = Field( # type: ignore
        default='https://schema.org/School',
        alias='@type',
        serialization_alias='@type'
    )
