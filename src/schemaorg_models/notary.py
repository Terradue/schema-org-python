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
from .legal_service import LegalService

class Notary(LegalService):
    '''
    A notary.
    '''
    class_: Literal['https://schema.org/Notary'] = Field( # type: ignore
        default='https://schema.org/Notary',
        alias='@type',
        serialization_alias='@type'
    )
