from __future__ import annotations

from .dose_schedule import DoseSchedule    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ReportedDoseSchedule(DoseSchedule):
    """
A patient-reported or observed dosing schedule for a drug or supplement.
    """
    class_: Literal['https://schema.org/ReportedDoseSchedule'] = Field( # type: ignore
        default='https://schema.org/ReportedDoseSchedule',
        alias='@type',
        serialization_alias='@type'
    )
