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

class PhysicalTherapy(MedicalTherapy):
    '''
    A process of progressive physical care and rehabilitation aimed at improving a health condition.
    '''
    class_: Literal['https://schema.org/PhysicalTherapy'] = Field( # type: ignore
        default='https://schema.org/PhysicalTherapy',
        alias='@type',
        serialization_alias='@type'
    )
