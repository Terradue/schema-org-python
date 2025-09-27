from typing import Literal
from pydantic import Field
from schemaorg_models.plan_action import PlanAction


class ReserveAction(PlanAction):
    """
Reserving a concrete object.\
\
Related actions:\
\
* [[ScheduleAction]]: Unlike ScheduleAction, ReserveAction reserves concrete objects (e.g. a table, a hotel) towards a time slot / spatial allocation.
    """
    type_: Literal['https://schema.org/ReserveAction'] = Field(default='https://schema.org/ReserveAction', alias='@type', serialization_alias='@type') # type: ignore
