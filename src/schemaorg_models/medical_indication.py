from typing import Literal
from pydantic import Field
from schemaorg_models.medical_entity import MedicalEntity


class MedicalIndication(MedicalEntity):
    """
A condition or factor that indicates use of a medical therapy, including signs, symptoms, risk factors, anatomical states, etc.
    """
    class_: Literal['https://schema.org/MedicalIndication'] = Field(default='https://schema.org/MedicalIndication', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
