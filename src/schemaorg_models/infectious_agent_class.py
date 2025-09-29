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
from .medical_enumeration import MedicalEnumeration

class InfectiousAgentClass(MedicalEnumeration):
    '''
    Classes of agents or pathogens that transmit infectious diseases. Enumerated type.
    '''
    class_: Literal['https://schema.org/InfectiousAgentClass'] = Field( # type: ignore
        default='https://schema.org/InfectiousAgentClass',
        alias='@type',
        serialization_alias='@type'
    )
