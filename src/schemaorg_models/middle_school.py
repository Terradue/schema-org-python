from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .educational_organization import EducationalOrganization

class MiddleSchool(EducationalOrganization):
    """
A middle school (typically for children aged around 11-14, although this varies somewhat).
    """
    class_: Literal['https://schema.org/MiddleSchool'] = Field( # type: ignore
        default='https://schema.org/MiddleSchool',
        alias='@type',
        serialization_alias='@type'
    )
