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
from .medical_organization import MedicalOrganization

class Pharmacy(MedicalOrganization):
    '''
    A pharmacy or drugstore.
    '''
    class_: Literal['https://schema.org/Pharmacy'] = Field( # type: ignore
        default='https://schema.org/Pharmacy',
        alias='@type',
        serialization_alias='@type'
    )
