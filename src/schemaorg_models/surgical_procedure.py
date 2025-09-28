from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_procedure import MedicalProcedure

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SurgicalProcedure(MedicalProcedure):
    """
A medical procedure involving an incision with instruments; performed for diagnose, or therapeutic purposes.
    """
    class_: Literal['https://schema.org/SurgicalProcedure'] = Field( # type: ignore
        default='https://schema.org/SurgicalProcedure',
        alias='@type',
        serialization_alias='@type'
    )
