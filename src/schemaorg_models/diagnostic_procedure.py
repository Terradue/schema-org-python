from __future__ import annotations

from .medical_procedure import MedicalProcedure    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DiagnosticProcedure(MedicalProcedure):
    """
A medical procedure intended primarily for diagnostic, as opposed to therapeutic, purposes.
    """
    class_: Literal['https://schema.org/DiagnosticProcedure'] = Field( # type: ignore
        default='https://schema.org/DiagnosticProcedure',
        alias='@type',
        serialization_alias='@type'
    )
