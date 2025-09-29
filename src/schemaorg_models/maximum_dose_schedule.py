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

class MaximumDoseSchedule(DoseSchedule):
    '''
    The maximum dosing schedule considered safe for a drug or supplement as recommended by an authority or by the drug/supplement's manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.
    '''
    class_: Literal['https://schema.org/MaximumDoseSchedule'] = Field( # type: ignore
        default='https://schema.org/MaximumDoseSchedule',
        alias='@type',
        serialization_alias='@type'
    )
