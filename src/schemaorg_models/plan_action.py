from typing import List, Literal, Optional, Union
from datetime import date, datetime
from pydantic import AliasChoices, Field
from schemaorg_models.organize_action import OrganizeAction


class PlanAction(OrganizeAction):
    """
The act of planning the execution of an event/task/action/reservation/plan to a future date.
    """
    class_: Literal['https://schema.org/PlanAction'] = Field(default='https://schema.org/PlanAction', alias='@type', serialization_alias='@type') # type: ignore
    scheduledTime: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('scheduledTime', 'https://schema.org/scheduledTime'), serialization_alias='https://schema.org/scheduledTime')
