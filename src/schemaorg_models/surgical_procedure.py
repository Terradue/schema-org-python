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
from .medical_procedure import MedicalProcedure

class SurgicalProcedure(MedicalProcedure):
    '''
    A medical procedure involving an incision with instruments; performed for diagnose, or therapeutic purposes.
    '''
    class_: Literal['https://schema.org/SurgicalProcedure'] = Field( # type: ignore
        default='https://schema.org/SurgicalProcedure',
        alias='@type',
        serialization_alias='@type'
    )
