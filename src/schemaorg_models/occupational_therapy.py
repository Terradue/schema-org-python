from typing import Literal
from pydantic import Field
from schemaorg_models.medical_therapy import MedicalTherapy


class OccupationalTherapy(MedicalTherapy):
    """
A treatment of people with physical, emotional, or social problems, using purposeful activity to help them overcome or learn to deal with their problems.
    """
    type_: Literal['https://schema.org/OccupationalTherapy'] = Field(default='https://schema.org/OccupationalTherapy', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
