from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_business import MedicalBusiness


class Optician(MedicalBusiness):
    """
A store that sells reading glasses and similar devices for improving vision.
    """
    type_: Literal['https://schema.org/Optician'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Optician'),serialization_alias='class') # type: ignore
