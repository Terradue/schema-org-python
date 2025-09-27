from typing import Literal
from pydantic import Field
from schemaorg_models.medical_business import MedicalBusiness


class Dentist(MedicalBusiness):
    """
A dentist.
    """
    type_: Literal['https://schema.org/Dentist'] = Field(default='https://schema.org/Dentist', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
