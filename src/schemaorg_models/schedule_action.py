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

class ScheduleAction(PlanAction):
    '''
    Scheduling future actions, events, or tasks.\
\
Related actions:\
\
* [[ReserveAction]]: Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task, etc) towards a time slot / spatial allocation.
    '''
    class_: Literal['https://schema.org/ScheduleAction'] = Field( # type: ignore
        default='https://schema.org/ScheduleAction',
        alias='@type',
        serialization_alias='@type'
    )
