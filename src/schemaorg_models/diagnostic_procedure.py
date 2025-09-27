from typing import Literal
from pydantic import Field
from schemaorg_models.medical_procedure import MedicalProcedure


class DiagnosticProcedure(MedicalProcedure):
    """
A medical procedure intended primarily for diagnostic, as opposed to therapeutic, purposes.
    """
    class_: Literal['https://schema.org/DiagnosticProcedure'] = Field(default='https://schema.org/DiagnosticProcedure', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
