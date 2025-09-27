from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalObservationalStudyDesign(MedicalEnumeration):
    """
Design models for observational medical studies. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalObservationalStudyDesign'] = Field(default='https://schema.org/MedicalObservationalStudyDesign', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
