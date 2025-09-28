from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_guideline import MedicalGuideline

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MedicalGuidelineContraindication(MedicalGuideline):
    """
A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound.
    """
    class_: Literal['https://schema.org/MedicalGuidelineContraindication'] = Field( # type: ignore
        default='https://schema.org/MedicalGuidelineContraindication',
        alias='@type',
        serialization_alias='@type'
    )
