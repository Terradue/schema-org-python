from typing import Literal
from pydantic import Field
from schemaorg_models.medical_organization import MedicalOrganization


class Pharmacy(MedicalOrganization):
    """
A pharmacy or drugstore.
    """
    type_: Literal['https://schema.org/Pharmacy'] = Field(default='https://schema.org/Pharmacy', alias='@type', serialization_alias='@type') # type: ignore
