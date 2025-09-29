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
from .audience import Audience

class MedicalAudience(Audience):
    '''
    Target audiences for medical web pages.
    '''
    class_: Literal['https://schema.org/MedicalAudience'] = Field( # type: ignore
        default='https://schema.org/MedicalAudience',
        alias='@type',
        serialization_alias='@type'
    )
