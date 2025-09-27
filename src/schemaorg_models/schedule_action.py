from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.plan_action import PlanAction


class ScheduleAction(PlanAction):
    """
Scheduling future actions, events, or tasks.\
\
Related actions:\
\
* [[ReserveAction]]: Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task, etc) towards a time slot / spatial allocation.
    """
    type_: Literal['https://schema.org/ScheduleAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ScheduleAction'),serialization_alias='class') # type: ignore
