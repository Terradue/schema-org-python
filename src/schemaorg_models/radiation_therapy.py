from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_therapy import MedicalTherapy


class RadiationTherapy(MedicalTherapy):
    """
A process of care using radiation aimed at improving a health condition.
    """
    type_: Literal['https://schema.org/RadiationTherapy'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RadiationTherapy'),serialization_alias='class') # type: ignore
