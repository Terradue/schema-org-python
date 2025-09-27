from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.specialty import Specialty


class MedicalSpecialty(Specialty):
    """
Any specific branch of medical science or practice. Medical specialities include clinical specialties that pertain to particular organ systems and their respective disease states, as well as allied health specialties. Enumerated type.
    """
    type_: Literal['https://schema.org/MedicalSpecialty'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalSpecialty'),serialization_alias='class') # type: ignore
