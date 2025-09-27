from typing import Literal
from pydantic import Field
from schemaorg_models.medical_procedure import MedicalProcedure


class DiagnosticProcedure(MedicalProcedure):
    """
A medical procedure intended primarily for diagnostic, as opposed to therapeutic, purposes.
    """
    class_: Literal['https://schema.org/DiagnosticProcedure'] = Field(default='https://schema.org/DiagnosticProcedure', alias='@type', serialization_alias='@type') # type: ignore
