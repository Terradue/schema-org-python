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

class PhysicalTherapy(MedicalTherapy):
    """
A process of progressive physical care and rehabilitation aimed at improving a health condition.
    """
    class_: Literal['https://schema.org/PhysicalTherapy'] = Field( # type: ignore
        default='https://schema.org/PhysicalTherapy',
        alias='@type',
        serialization_alias='@type'
    )
