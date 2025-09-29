from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .educational_organization import EducationalOrganization

class CollegeOrUniversity(EducationalOrganization):
    '''
    A college, university, or other third-level educational institution.
    '''
    class_: Literal['https://schema.org/CollegeOrUniversity'] = Field( # type: ignore
        default='https://schema.org/CollegeOrUniversity',
        alias='@type',
        serialization_alias='@type'
    )
