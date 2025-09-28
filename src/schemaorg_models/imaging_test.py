from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_test import MedicalTest

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

class ImagingTest(MedicalTest):
    """
Any medical imaging modality typically used for diagnostic purposes.
    """
    class_: Literal['https://schema.org/ImagingTest'] = Field( # type: ignore
        default='https://schema.org/ImagingTest',
        alias='@type',
        serialization_alias='@type'
    )
    imagingTechnique: Optional[Union["MedicalImagingTechnique", List["MedicalImagingTechnique"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'imagingTechnique',
            'https://schema.org/imagingTechnique'
        ),
        serialization_alias='https://schema.org/imagingTechnique'
    )
