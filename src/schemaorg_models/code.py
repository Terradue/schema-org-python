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
from .creative_work import CreativeWork

class Code(CreativeWork):
    '''
    Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates.
    '''
    class_: Literal['https://schema.org/Code'] = Field( # type: ignore
        default='https://schema.org/Code',
        alias='@type',
        serialization_alias='@type'
    )
