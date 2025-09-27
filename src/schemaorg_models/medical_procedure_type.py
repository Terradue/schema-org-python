from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalProcedureType(MedicalEnumeration):
    """
An enumeration that describes different types of medical procedures.
    """
    type_: Literal['https://schema.org/MedicalProcedureType'] = Field(default='https://schema.org/MedicalProcedureType', alias='@type', serialization_alias='@type') # type: ignore
