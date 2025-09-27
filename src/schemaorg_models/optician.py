from typing import Literal
from pydantic import Field
from schemaorg_models.medical_business import MedicalBusiness


class Optician(MedicalBusiness):
    """
A store that sells reading glasses and similar devices for improving vision.
    """
    class_: Literal['https://schema.org/Optician'] = Field(default='https://schema.org/Optician', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
