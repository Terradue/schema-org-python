from typing import Literal
from pydantic import Field
from schemaorg_models.medical_therapy import MedicalTherapy


class PhysicalTherapy(MedicalTherapy):
    """
A process of progressive physical care and rehabilitation aimed at improving a health condition.
    """
    class_: Literal['https://schema.org/PhysicalTherapy'] = Field(default='https://schema.org/PhysicalTherapy', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
