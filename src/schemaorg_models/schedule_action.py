from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.plan_action import PlanAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ScheduleAction(PlanAction):
    """
Scheduling future actions, events, or tasks.\
\
Related actions:\
\
* [[ReserveAction]]: Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task, etc) towards a time slot / spatial allocation.
    """
    class_: Literal['https://schema.org/ScheduleAction'] = Field( # type: ignore
        default='https://schema.org/ScheduleAction',
        alias='@type',
        serialization_alias='@type'
    )
