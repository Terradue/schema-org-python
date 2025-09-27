from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_business import MedicalBusiness


class Dentist(MedicalBusiness):
    """
A dentist.
    """
    type_: Literal['https://schema.org/Dentist'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Dentist'),serialization_alias='class') # type: ignore
