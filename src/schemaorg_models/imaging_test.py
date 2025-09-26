from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.medical_test import MedicalTest


class ImagingTest(MedicalTest):
    """
Any medical imaging modality typically used for diagnostic purposes.
    """
    imagingTechnique: Optional[Union["MedicalImagingTechnique", List["MedicalImagingTechnique"]]] = Field(default=None,validation_alias=AliasChoices('imagingTechnique', 'https://schema.org/imagingTechnique'),serialization_alias='https://schema.org/imagingTechnique')
