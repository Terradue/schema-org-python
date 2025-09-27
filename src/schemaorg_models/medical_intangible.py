from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_entity import MedicalEntity


class MedicalIntangible(MedicalEntity):
    """
A utility class that serves as the umbrella for a number of 'intangible' things in the medical space.
    """
    type_: Literal['https://schema.org/MedicalIntangible'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalIntangible'),serialization_alias='class') # type: ignore
