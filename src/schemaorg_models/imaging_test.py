from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
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
    '''
    Any medical imaging modality typically used for diagnostic purposes.

    Attributes:
        imagingTechnique: Imaging technique used.
    '''
    class_: Literal['https://schema.org/ImagingTest'] = Field( # type: ignore
        default='https://schema.org/ImagingTest',
        alias='@type',
        serialization_alias='@type'
    )
    imagingTechnique: Optional[Union['MedicalImagingTechnique', List['MedicalImagingTechnique']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
