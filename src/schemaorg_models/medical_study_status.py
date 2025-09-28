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

class MedicalStudyStatus(MedicalEnumeration):
    """
The status of a medical study. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalStudyStatus'] = Field( # type: ignore
        default='https://schema.org/MedicalStudyStatus',
        alias='@type',
        serialization_alias='@type'
    )
