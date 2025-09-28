from __future__ import annotations

from .plan_action import PlanAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ReserveAction(PlanAction):
    """
Reserving a concrete object.\
\
Related actions:\
\
* [[ScheduleAction]]: Unlike ScheduleAction, ReserveAction reserves concrete objects (e.g. a table, a hotel) towards a time slot / spatial allocation.
    """
    class_: Literal['https://schema.org/ReserveAction'] = Field( # type: ignore
        default='https://schema.org/ReserveAction',
        alias='@type',
        serialization_alias='@type'
    )
