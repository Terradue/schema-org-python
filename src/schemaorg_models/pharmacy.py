from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_organization import MedicalOrganization

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Pharmacy(MedicalOrganization):
    """
A pharmacy or drugstore.
    """
    class_: Literal['https://schema.org/Pharmacy'] = Field( # type: ignore
        default='https://schema.org/Pharmacy',
        alias='@type',
        serialization_alias='@type'
    )
