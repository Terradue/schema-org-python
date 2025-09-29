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

class Attorney(LegalService):
    '''
    Professional service: Attorney. \
\
This type is deprecated - [[LegalService]] is more inclusive and less ambiguous.
    '''
    class_: Literal['https://schema.org/Attorney'] = Field( # type: ignore
        default='https://schema.org/Attorney',
        alias='@type',
        serialization_alias='@type'
    )
