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
from .plan_action import PlanAction

class ReserveAction(PlanAction):
    '''
    Reserving a concrete object.\
\
Related actions:\
\
* [[ScheduleAction]]: Unlike ScheduleAction, ReserveAction reserves concrete objects (e.g. a table, a hotel) towards a time slot / spatial allocation.
    '''
    class_: Literal['https://schema.org/ReserveAction'] = Field( # type: ignore
        default='https://schema.org/ReserveAction',
        alias='@type',
        serialization_alias='@type'
    )
