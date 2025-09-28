from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .medical_test import MedicalTest
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_imaging_technique import MedicalImagingTechnique

class ImagingTest(MedicalTest):
    """
Any medical imaging modality typically used for diagnostic purposes.
    """
    class_: Literal['https://schema.org/ImagingTest'] = Field( # type: ignore
        default='https://schema.org/ImagingTest',
        alias='@type',
        serialization_alias='@type'
    )
    imagingTechnique: Optional[Union[MedicalImagingTechnique, List[MedicalImagingTechnique]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'imagingTechnique',
            'https://schema.org/imagingTechnique'
        ),
        serialization_alias='https://schema.org/imagingTechnique'
    )
