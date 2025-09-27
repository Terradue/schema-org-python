from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_procedure import MedicalProcedure


class SurgicalProcedure(MedicalProcedure):
    """
A medical procedure involving an incision with instruments; performed for diagnose, or therapeutic purposes.
    """
    type_: Literal['https://schema.org/SurgicalProcedure'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SurgicalProcedure'),serialization_alias='class') # type: ignore
