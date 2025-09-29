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
from .administrative_area import AdministrativeArea

class SchoolDistrict(AdministrativeArea):
    '''
    A School District is an administrative area for the administration of schools.
    '''
    class_: Literal['https://schema.org/SchoolDistrict'] = Field( # type: ignore
        default='https://schema.org/SchoolDistrict',
        alias='@type',
        serialization_alias='@type'
    )
