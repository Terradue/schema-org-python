from typing import Literal
from pydantic import Field
from schemaorg_models.medical_therapy import MedicalTherapy


class RadiationTherapy(MedicalTherapy):
    """
A process of care using radiation aimed at improving a health condition.
    """
    class_: Literal['https://schema.org/RadiationTherapy'] = Field('class', alias='class', serialization_alias='class') # type: ignore
