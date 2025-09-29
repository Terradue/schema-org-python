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

class Plumber(HomeAndConstructionBusiness):
    '''
    A plumbing service.
    '''
    class_: Literal['https://schema.org/Plumber'] = Field( # type: ignore
        default='https://schema.org/Plumber',
        alias='@type',
        serialization_alias='@type'
    )
