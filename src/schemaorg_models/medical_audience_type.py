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

class MedicalAudienceType(MedicalEnumeration):
    """
Target audiences types for medical web pages. Enumerated type.
    """
    class_: Literal['https://schema.org/MedicalAudienceType'] = Field( # type: ignore
        default='https://schema.org/MedicalAudienceType',
        alias='@type',
        serialization_alias='@type'
    )
