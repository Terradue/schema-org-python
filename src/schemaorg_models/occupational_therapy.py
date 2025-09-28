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

class OccupationalTherapy(MedicalTherapy):
    """
A treatment of people with physical, emotional, or social problems, using purposeful activity to help them overcome or learn to deal with their problems.
    """
    class_: Literal['https://schema.org/OccupationalTherapy'] = Field( # type: ignore
        default='https://schema.org/OccupationalTherapy',
        alias='@type',
        serialization_alias='@type'
    )
