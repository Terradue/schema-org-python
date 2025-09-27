from typing import Literal
from pydantic import Field
from schemaorg_models.medical_organization import MedicalOrganization


class VeterinaryCare(MedicalOrganization):
    """
A vet's office.
    """
    type_: Literal['https://schema.org/VeterinaryCare'] = Field(default='https://schema.org/VeterinaryCare', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
