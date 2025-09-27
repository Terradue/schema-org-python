from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.medical_enumeration import MedicalEnumeration


class MedicalImagingTechnique(MedicalEnumeration):
    """
Any medical imaging modality typically used for diagnostic purposes. Enumerated type.
    """
    type_: Literal['https://schema.org/MedicalImagingTechnique'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalImagingTechnique'),serialization_alias='class') # type: ignore
