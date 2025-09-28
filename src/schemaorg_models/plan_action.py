from __future__ import annotations
from datetime import (
    date,
    datetime
)
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .organize_action import OrganizeAction

class PlanAction(OrganizeAction):
    """
The act of planning the execution of an event/task/action/reservation/plan to a future date.
    """
    class_: Literal['https://schema.org/PlanAction'] = Field( # type: ignore
        default='https://schema.org/PlanAction',
        alias='@type',
        serialization_alias='@type'
    )
    scheduledTime: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'scheduledTime',
            'https://schema.org/scheduledTime'
        ),
        serialization_alias='https://schema.org/scheduledTime'
    )
