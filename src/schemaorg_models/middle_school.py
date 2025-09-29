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

class MiddleSchool(EducationalOrganization):
    '''
    A middle school (typically for children aged around 11-14, although this varies somewhat).
    '''
    class_: Literal['https://schema.org/MiddleSchool'] = Field( # type: ignore
        default='https://schema.org/MiddleSchool',
        alias='@type',
        serialization_alias='@type'
    )
