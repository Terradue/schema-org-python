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

class LifestyleModification(MedicalEntity):
    '''
    A process of care involving exercise, changes to diet, fitness routines, and other lifestyle changes aimed at improving a health condition.
    '''
    class_: Literal['https://schema.org/LifestyleModification'] = Field( # type: ignore
        default='https://schema.org/LifestyleModification',
        alias='@type',
        serialization_alias='@type'
    )
