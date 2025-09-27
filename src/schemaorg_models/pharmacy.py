from typing import Literal
from pydantic import Field
from schemaorg_models.medical_organization import MedicalOrganization


class Pharmacy(MedicalOrganization):
    """
A pharmacy or drugstore.
    """
    class_: Literal['https://schema.org/Pharmacy'] = Field('class', alias='class', serialization_alias='class') # type: ignore
