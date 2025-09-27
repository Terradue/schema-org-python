from typing import Literal
from pydantic import Field
from schemaorg_models.medical_therapy import MedicalTherapy


class RadiationTherapy(MedicalTherapy):
    """
A process of care using radiation aimed at improving a health condition.
    """
    class_: Literal['https://schema.org/RadiationTherapy'] = Field(default='https://schema.org/RadiationTherapy', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
