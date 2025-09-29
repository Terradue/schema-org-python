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
from .place import Place

class AdministrativeArea(Place):
    '''
    A geographical region, typically under the jurisdiction of a particular government.
    '''
    class_: Literal['https://schema.org/AdministrativeArea'] = Field( # type: ignore
        default='https://schema.org/AdministrativeArea',
        alias='@type',
        serialization_alias='@type'
    )
