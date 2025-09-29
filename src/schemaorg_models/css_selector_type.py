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

class CssSelectorType(BaseModel):
    '''
    Text representing a CSS selector.
    '''
    class_: Literal['https://schema.org/CssSelectorType'] = Field( # type: ignore
        default='https://schema.org/CssSelectorType',
        alias='@type',
        serialization_alias='@type'
    )
