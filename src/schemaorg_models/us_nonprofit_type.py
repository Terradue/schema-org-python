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

class USNonprofitType(NonprofitType):
    '''
    USNonprofitType: Non-profit organization type originating from the United States.
    '''
    class_: Literal['https://schema.org/USNonprofitType'] = Field( # type: ignore
        default='https://schema.org/USNonprofitType',
        alias='@type',
        serialization_alias='@type'
    )
