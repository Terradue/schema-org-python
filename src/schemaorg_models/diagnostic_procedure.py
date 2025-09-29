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

class DiagnosticProcedure(MedicalProcedure):
    '''
    A medical procedure intended primarily for diagnostic, as opposed to therapeutic, purposes.
    '''
    class_: Literal['https://schema.org/DiagnosticProcedure'] = Field( # type: ignore
        default='https://schema.org/DiagnosticProcedure',
        alias='@type',
        serialization_alias='@type'
    )
