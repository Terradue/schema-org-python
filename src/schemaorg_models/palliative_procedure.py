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
from .medical_therapy import MedicalTherapy

class PalliativeProcedure(MedicalTherapy):
    '''
    A medical procedure intended primarily for palliative purposes, aimed at relieving the symptoms of an underlying health condition.
    '''
    class_: Literal['https://schema.org/PalliativeProcedure'] = Field( # type: ignore
        default='https://schema.org/PalliativeProcedure',
        alias='@type',
        serialization_alias='@type'
    )
