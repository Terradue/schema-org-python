from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .educational_organization import EducationalOrganization

class Preschool(EducationalOrganization):
    """
A preschool.
    """
    class_: Literal['https://schema.org/Preschool'] = Field( # type: ignore
        default='https://schema.org/Preschool',
        alias='@type',
        serialization_alias='@type'
    )
