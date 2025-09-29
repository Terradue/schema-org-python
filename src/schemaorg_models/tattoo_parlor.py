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
from .health_and_beauty_business import HealthAndBeautyBusiness

class TattooParlor(HealthAndBeautyBusiness):
    '''
    A tattoo parlor.
    '''
    class_: Literal['https://schema.org/TattooParlor'] = Field( # type: ignore
        default='https://schema.org/TattooParlor',
        alias='@type',
        serialization_alias='@type'
    )
