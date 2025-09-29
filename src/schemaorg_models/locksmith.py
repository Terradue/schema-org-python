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
from .home_and_construction_business import HomeAndConstructionBusiness

class Locksmith(HomeAndConstructionBusiness):
    '''
    A locksmith.
    '''
    class_: Literal['https://schema.org/Locksmith'] = Field( # type: ignore
        default='https://schema.org/Locksmith',
        alias='@type',
        serialization_alias='@type'
    )
