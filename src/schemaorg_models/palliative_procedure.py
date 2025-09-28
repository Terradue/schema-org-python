from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_therapy import MedicalTherapy

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PalliativeProcedure(MedicalTherapy):
    """
A medical procedure intended primarily for palliative purposes, aimed at relieving the symptoms of an underlying health condition.
    """
    class_: Literal['https://schema.org/PalliativeProcedure'] = Field( # type: ignore
        default='https://schema.org/PalliativeProcedure',
        alias='@type',
        serialization_alias='@type'
    )
