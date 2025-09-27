from typing import Literal
from pydantic import Field
from schemaorg_models.medical_entity import MedicalEntity


class LifestyleModification(MedicalEntity):
    """
A process of care involving exercise, changes to diet, fitness routines, and other lifestyle changes aimed at improving a health condition.
    """
    class_: Literal['https://schema.org/LifestyleModification'] = Field(default='https://schema.org/LifestyleModification', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
