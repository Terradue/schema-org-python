from typing import Literal
from pydantic import Field
from schemaorg_models.medical_organization import MedicalOrganization


class VeterinaryCare(MedicalOrganization):
    """
A vet's office.
    """
    class_: Literal['https://schema.org/VeterinaryCare'] = Field(default='https://schema.org/VeterinaryCare', alias='class', serialization_alias='class') # type: ignore
