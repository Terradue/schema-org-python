from typing import Literal
from pydantic import Field
from schemaorg_models.specialty import Specialty


class MedicalSpecialty(Specialty):
    """
Any specific branch of medical science or practice. Medical specialities include clinical specialties that pertain to particular organ systems and their respective disease states, as well as allied health specialties. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalSpecialty'] = Field(default='https://schema.org/MedicalSpecialty', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
