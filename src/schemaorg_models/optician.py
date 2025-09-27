from typing import Literal
from pydantic import Field
from schemaorg_models.medical_business import MedicalBusiness


class Optician(MedicalBusiness):
    """
A store that sells reading glasses and similar devices for improving vision.
    """
    class_: Literal['https://schema.org/Optician'] = Field('class', alias='class', serialization_alias='class') # type: ignore
