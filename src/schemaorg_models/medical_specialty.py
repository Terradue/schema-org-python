from typing import Literal
from pydantic import Field
from schemaorg_models.specialty import Specialty


class MedicalSpecialty(Specialty):
    """
Any specific branch of medical science or practice. Medical specialities include clinical specialties that pertain to particular organ systems and their respective disease states, as well as allied health specialties. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalSpecialty'] = Field(default='https://schema.org/MedicalSpecialty', alias='class', serialization_alias='class') # type: ignore
