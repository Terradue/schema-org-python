from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.dose_schedule import DoseSchedule

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MaximumDoseSchedule(DoseSchedule):
    """
The maximum dosing schedule considered safe for a drug or supplement as recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.
    """
    class_: Literal['https://schema.org/MaximumDoseSchedule'] = Field( # type: ignore
        default='https://schema.org/MaximumDoseSchedule',
        alias='@type',
        serialization_alias='@type'
    )
