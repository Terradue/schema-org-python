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

class VeterinaryCare(MedicalOrganization):
    '''
    A vet's office.
    '''
    class_: Literal['https://schema.org/VeterinaryCare'] = Field( # type: ignore
        default='https://schema.org/VeterinaryCare',
        alias='@type',
        serialization_alias='@type'
    )
