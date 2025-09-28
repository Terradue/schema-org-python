from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_business import MedicalBusiness

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Optician(MedicalBusiness):
    """
A store that sells reading glasses and similar devices for improving vision.
    """
    class_: Literal['https://schema.org/Optician'] = Field( # type: ignore
        default='https://schema.org/Optician',
        alias='@type',
        serialization_alias='@type'
    )
