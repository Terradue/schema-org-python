from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_entity import MedicalEntity


class LifestyleModification(MedicalEntity):
    """
A process of care involving exercise, changes to diet, fitness routines, and other lifestyle changes aimed at improving a health condition.
    """
    type_: Literal['https://schema.org/LifestyleModification'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/LifestyleModification'),serialization_alias='class') # type: ignore
