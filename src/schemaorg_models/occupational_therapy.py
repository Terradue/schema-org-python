from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_therapy import MedicalTherapy


class OccupationalTherapy(MedicalTherapy):
    """
A treatment of people with physical, emotional, or social problems, using purposeful activity to help them overcome or learn to deal with their problems.
    """
    type_: Literal['https://schema.org/OccupationalTherapy'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OccupationalTherapy'),serialization_alias='class') # type: ignore
