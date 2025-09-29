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

class SelfStorage(LocalBusiness):
    '''
    A self-storage facility.
    '''
    class_: Literal['https://schema.org/SelfStorage'] = Field( # type: ignore
        default='https://schema.org/SelfStorage',
        alias='@type',
        serialization_alias='@type'
    )
