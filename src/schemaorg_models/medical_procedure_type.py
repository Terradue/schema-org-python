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

class MedicalProcedureType(MedicalEnumeration):
    """
An enumeration that describes different types of medical procedures.
    """
    class_: Literal['https://schema.org/MedicalProcedureType'] = Field( # type: ignore
        default='https://schema.org/MedicalProcedureType',
        alias='@type',
        serialization_alias='@type'
    )
