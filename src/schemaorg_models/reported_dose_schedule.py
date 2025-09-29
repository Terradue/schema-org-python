from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .dose_schedule import DoseSchedule

class ReportedDoseSchedule(DoseSchedule):
    '''
    A patient-reported or observed dosing schedule for a drug or supplement.
    '''
    class_: Literal['https://schema.org/ReportedDoseSchedule'] = Field( # type: ignore
        default='https://schema.org/ReportedDoseSchedule',
        alias='@type',
        serialization_alias='@type'
    )
