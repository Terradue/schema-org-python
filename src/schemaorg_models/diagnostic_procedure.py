from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_procedure import MedicalProcedure


class DiagnosticProcedure(MedicalProcedure):
    """
A medical procedure intended primarily for diagnostic, as opposed to therapeutic, purposes.
    """
    type_: Literal['https://schema.org/DiagnosticProcedure'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DiagnosticProcedure'),serialization_alias='class') # type: ignore
