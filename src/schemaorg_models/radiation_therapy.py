from typing import Literal
from pydantic import Field
from schemaorg_models.medical_therapy import MedicalTherapy


class RadiationTherapy(MedicalTherapy):
    """
A process of care using radiation aimed at improving a health condition.
    """
    type_: Literal['https://schema.org/RadiationTherapy'] = Field(default='https://schema.org/RadiationTherapy', alias='@type', serialization_alias='@type') # type: ignore
