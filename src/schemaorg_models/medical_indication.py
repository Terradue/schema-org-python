from typing import Literal
from pydantic import Field
from schemaorg_models.medical_entity import MedicalEntity


class MedicalIndication(MedicalEntity):
    """
A condition or factor that indicates use of a medical therapy, including signs, symptoms, risk factors, anatomical states, etc.
    """
    type_: Literal['https://schema.org/MedicalIndication'] = Field(default='https://schema.org/MedicalIndication', alias='@type', serialization_alias='@type') # type: ignore
