from typing import Literal
from pydantic import Field
from schemaorg_models.medical_procedure import MedicalProcedure


class SurgicalProcedure(MedicalProcedure):
    """
A medical procedure involving an incision with instruments; performed for diagnose, or therapeutic purposes.
    """
    type_: Literal['https://schema.org/SurgicalProcedure'] = Field(default='https://schema.org/SurgicalProcedure', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
