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

class Preschool(EducationalOrganization):
    '''
    A preschool.
    '''
    class_: Literal['https://schema.org/Preschool'] = Field( # type: ignore
        default='https://schema.org/Preschool',
        alias='@type',
        serialization_alias='@type'
    )
