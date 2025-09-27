from typing import Literal
from pydantic import Field
from schemaorg_models.medical_entity import MedicalEntity


class MedicalIntangible(MedicalEntity):
    """
A utility class that serves as the umbrella for a number of 'intangible' things in the medical space.
    """
    class_: Literal['https://schema.org/MedicalIntangible'] = Field(default='https://schema.org/MedicalIntangible', alias='class', serialization_alias='class') # type: ignore
