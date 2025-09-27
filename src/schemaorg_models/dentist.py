from typing import Literal
from pydantic import Field
from schemaorg_models.medical_business import MedicalBusiness


class Dentist(MedicalBusiness):
    """
A dentist.
    """
    class_: Literal['https://schema.org/Dentist'] = Field(default='https://schema.org/Dentist', alias='@type', serialization_alias='@type') # type: ignore
