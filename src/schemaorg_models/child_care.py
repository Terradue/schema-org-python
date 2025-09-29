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

class ChildCare(LocalBusiness):
    '''
    A Childcare center.
    '''
    class_: Literal['https://schema.org/ChildCare'] = Field( # type: ignore
        default='https://schema.org/ChildCare',
        alias='@type',
        serialization_alias='@type'
    )
