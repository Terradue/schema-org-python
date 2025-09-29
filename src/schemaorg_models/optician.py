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
from .medical_business import MedicalBusiness

class Optician(MedicalBusiness):
    '''
    A store that sells reading glasses and similar devices for improving vision.
    '''
    class_: Literal['https://schema.org/Optician'] = Field( # type: ignore
        default='https://schema.org/Optician',
        alias='@type',
        serialization_alias='@type'
    )
