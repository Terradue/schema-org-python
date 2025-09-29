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
from .store import Store

class MobilePhoneStore(Store):
    '''
    A store that sells mobile phones and related accessories.
    '''
    class_: Literal['https://schema.org/MobilePhoneStore'] = Field( # type: ignore
        default='https://schema.org/MobilePhoneStore',
        alias='@type',
        serialization_alias='@type'
    )
