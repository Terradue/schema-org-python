from __future__ import annotations

from .therapeutic_procedure import TherapeuticProcedure    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PsychologicalTreatment(TherapeuticProcedure):
    """
A process of care relying upon counseling, dialogue and communication  aimed at improving a mental health condition without use of drugs.
    """
    class_: Literal['https://schema.org/PsychologicalTreatment'] = Field( # type: ignore
        default='https://schema.org/PsychologicalTreatment',
        alias='@type',
        serialization_alias='@type'
    )
