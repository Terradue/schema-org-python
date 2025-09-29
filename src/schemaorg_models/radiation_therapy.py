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

class RadiationTherapy(MedicalTherapy):
    '''
    A process of care using radiation aimed at improving a health condition.
    '''
    class_: Literal['https://schema.org/RadiationTherapy'] = Field( # type: ignore
        default='https://schema.org/RadiationTherapy',
        alias='@type',
        serialization_alias='@type'
    )
