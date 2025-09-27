from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_organization import MedicalOrganization


class Pharmacy(MedicalOrganization):
    """
A pharmacy or drugstore.
    """
    type_: Literal['https://schema.org/Pharmacy'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Pharmacy'),serialization_alias='class') # type: ignore
