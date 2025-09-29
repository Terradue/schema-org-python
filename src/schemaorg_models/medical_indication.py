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

class MedicalIndication(MedicalEntity):
    '''
    A condition or factor that indicates use of a medical therapy, including signs, symptoms, risk factors, anatomical states, etc.
    '''
    class_: Literal['https://schema.org/MedicalIndication'] = Field( # type: ignore
        default='https://schema.org/MedicalIndication',
        alias='@type',
        serialization_alias='@type'
    )
