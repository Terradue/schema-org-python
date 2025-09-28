from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .educational_organization import EducationalOrganization

class ElementarySchool(EducationalOrganization):
    """
An elementary school.
    """
    class_: Literal['https://schema.org/ElementarySchool'] = Field( # type: ignore
        default='https://schema.org/ElementarySchool',
        alias='@type',
        serialization_alias='@type'
    )
