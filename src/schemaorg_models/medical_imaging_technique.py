from typing import Literal
from pydantic import Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalImagingTechnique(MedicalEnumeration):
    """
Any medical imaging modality typically used for diagnostic purposes. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalImagingTechnique'] = Field(default='https://schema.org/MedicalImagingTechnique', alias='class', serialization_alias='class') # type: ignore
