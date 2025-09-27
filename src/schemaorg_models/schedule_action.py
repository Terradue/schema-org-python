from typing import Literal
from pydantic import Field
from schemaorg_models.plan_action import PlanAction


class ScheduleAction(PlanAction):
    """
Scheduling future actions, events, or tasks.\
\
Related actions:\
\
* [[ReserveAction]]: Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task, etc) towards a time slot / spatial allocation.
    """
    class_: Literal['https://schema.org/ScheduleAction'] = Field(default='https://schema.org/ScheduleAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
