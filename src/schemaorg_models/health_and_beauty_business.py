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
from .local_business import LocalBusiness

class HealthAndBeautyBusiness(LocalBusiness):
    '''
    Health and beauty.
    '''
    class_: Literal['https://schema.org/HealthAndBeautyBusiness'] = Field( # type: ignore
        default='https://schema.org/HealthAndBeautyBusiness',
        alias='@type',
        serialization_alias='@type'
    )
