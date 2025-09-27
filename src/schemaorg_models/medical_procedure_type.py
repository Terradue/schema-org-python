from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalProcedureType(MedicalEnumeration):
    """
An enumeration that describes different types of medical procedures.
    """
    type_: Literal['https://schema.org/MedicalProcedureType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalProcedureType'),serialization_alias='class') # type: ignore
