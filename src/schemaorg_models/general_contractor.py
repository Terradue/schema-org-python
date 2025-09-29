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

class GeneralContractor(HomeAndConstructionBusiness):
    '''
    A general contractor.
    '''
    class_: Literal['https://schema.org/GeneralContractor'] = Field( # type: ignore
        default='https://schema.org/GeneralContractor',
        alias='@type',
        serialization_alias='@type'
    )
