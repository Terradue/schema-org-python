from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.medical_test import MedicalTest


class ImagingTest(MedicalTest):
    """
Any medical imaging modality typically used for diagnostic purposes.
    """
    class_: Literal['https://schema.org/ImagingTest'] = Field(default='https://schema.org/ImagingTest', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    imagingTechnique: Optional[Union["MedicalImagingTechnique", List["MedicalImagingTechnique"]]] = Field(default=None, validation_alias=AliasChoices('imagingTechnique', 'https://schema.org/imagingTechnique'), serialization_alias='https://schema.org/imagingTechnique')
