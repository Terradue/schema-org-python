from typing import Literal
from pydantic import Field
from schemaorg_models.medical_entity import MedicalEntity


class MedicalIndication(MedicalEntity):
    """
A condition or factor that indicates use of a medical therapy, including signs, symptoms, risk factors, anatomical states, etc.
    """
    class_: Literal['https://schema.org/MedicalIndication'] = Field('class', alias='class', serialization_alias='class') # type: ignore
