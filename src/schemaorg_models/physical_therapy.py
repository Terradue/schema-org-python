from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_therapy import MedicalTherapy


class PhysicalTherapy(MedicalTherapy):
    """
A process of progressive physical care and rehabilitation aimed at improving a health condition.
    """
    type_: Literal['https://schema.org/PhysicalTherapy'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PhysicalTherapy'),serialization_alias='class') # type: ignore
