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

class HVACBusiness(HomeAndConstructionBusiness):
    '''
    A business that provides Heating, Ventilation and Air Conditioning services.
    '''
    class_: Literal['https://schema.org/HVACBusiness'] = Field( # type: ignore
        default='https://schema.org/HVACBusiness',
        alias='@type',
        serialization_alias='@type'
    )
