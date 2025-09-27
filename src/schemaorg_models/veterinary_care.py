from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_organization import MedicalOrganization


class VeterinaryCare(MedicalOrganization):
    """
A vet's office.
    """
    type_: Literal['https://schema.org/VeterinaryCare'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/VeterinaryCare'),serialization_alias='class') # type: ignore
