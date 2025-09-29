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

class RecyclingCenter(LocalBusiness):
    '''
    A recycling center.
    '''
    class_: Literal['https://schema.org/RecyclingCenter'] = Field( # type: ignore
        default='https://schema.org/RecyclingCenter',
        alias='@type',
        serialization_alias='@type'
    )
