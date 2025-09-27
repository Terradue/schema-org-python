from typing import Literal
from pydantic import Field
from schemaorg_models.medical_therapy import MedicalTherapy


class PhysicalTherapy(MedicalTherapy):
    """
A process of progressive physical care and rehabilitation aimed at improving a health condition.
    """
    class_: Literal['https://schema.org/PhysicalTherapy'] = Field(default='https://schema.org/PhysicalTherapy', alias='@type', serialization_alias='@type') # type: ignore
