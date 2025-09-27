from typing import Literal
from pydantic import Field
from schemaorg_models.medical_organization import MedicalOrganization


class Pharmacy(MedicalOrganization):
    """
A pharmacy or drugstore.
    """
    class_: Literal['https://schema.org/Pharmacy'] = Field(default='https://schema.org/Pharmacy', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
