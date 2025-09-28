from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_indication import MedicalIndication

from pydantic import (
    Field
)
from typing import (
    Literal
)

class PreventionIndication(MedicalIndication):
    """
An indication for preventing an underlying condition, symptom, etc.
    """
    class_: Literal['https://schema.org/PreventionIndication'] = Field( # type: ignore
        default='https://schema.org/PreventionIndication',
        alias='@type',
        serialization_alias='@type'
    )
