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

class HighSchool(EducationalOrganization):
    '''
    A high school.
    '''
    class_: Literal['https://schema.org/HighSchool'] = Field( # type: ignore
        default='https://schema.org/HighSchool',
        alias='@type',
        serialization_alias='@type'
    )
