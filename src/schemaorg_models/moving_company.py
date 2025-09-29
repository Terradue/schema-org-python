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

class MovingCompany(HomeAndConstructionBusiness):
    '''
    A moving company.
    '''
    class_: Literal['https://schema.org/MovingCompany'] = Field( # type: ignore
        default='https://schema.org/MovingCompany',
        alias='@type',
        serialization_alias='@type'
    )
