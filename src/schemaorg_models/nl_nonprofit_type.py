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
from .nonprofit_type import NonprofitType

class NLNonprofitType(NonprofitType):
    '''
    NLNonprofitType: Non-profit organization type originating from the Netherlands.
    '''
    class_: Literal['https://schema.org/NLNonprofitType'] = Field( # type: ignore
        default='https://schema.org/NLNonprofitType',
        alias='@type',
        serialization_alias='@type'
    )
