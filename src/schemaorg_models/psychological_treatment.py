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
from .therapeutic_procedure import TherapeuticProcedure

class PsychologicalTreatment(TherapeuticProcedure):
    '''
    A process of care relying upon counseling, dialogue and communication  aimed at improving a mental health condition without use of drugs.
    '''
    class_: Literal['https://schema.org/PsychologicalTreatment'] = Field( # type: ignore
        default='https://schema.org/PsychologicalTreatment',
        alias='@type',
        serialization_alias='@type'
    )
