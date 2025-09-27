from typing import Literal
from pydantic import Field
from schemaorg_models.medical_procedure import MedicalProcedure


class SurgicalProcedure(MedicalProcedure):
    """
A medical procedure involving an incision with instruments; performed for diagnose, or therapeutic purposes.
    """
    class_: Literal['https://schema.org/SurgicalProcedure'] = Field(default='https://schema.org/SurgicalProcedure', alias='class', serialization_alias='class') # type: ignore
