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
from .medical_entity import MedicalEntity

class MedicalIntangible(MedicalEntity):
    '''
    A utility class that serves as the umbrella for a number of 'intangible' things in the medical space.
    '''
    class_: Literal['https://schema.org/MedicalIntangible'] = Field( # type: ignore
        default='https://schema.org/MedicalIntangible',
        alias='@type',
        serialization_alias='@type'
    )
