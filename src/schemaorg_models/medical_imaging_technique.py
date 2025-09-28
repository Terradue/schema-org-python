from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_enumeration import MedicalEnumeration

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MedicalImagingTechnique(MedicalEnumeration):
    """
Any medical imaging modality typically used for diagnostic purposes. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalImagingTechnique'] = Field( # type: ignore
        default='https://schema.org/MedicalImagingTechnique',
        alias='@type',
        serialization_alias='@type'
    )
