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

class DrugPrescriptionStatus(MedicalEnumeration):
    """
Indicates whether this drug is available by prescription or over-the-counter.
    """
    class_: Literal['https://schema.org/DrugPrescriptionStatus'] = Field( # type: ignore
        default='https://schema.org/DrugPrescriptionStatus',
        alias='@type',
        serialization_alias='@type'
    )
