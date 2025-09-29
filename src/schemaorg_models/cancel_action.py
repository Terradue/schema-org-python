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

class CancelAction(PlanAction):
    '''
    The act of asserting that a future event/action is no longer going to happen.\
\
Related actions:\
\
* [[ConfirmAction]]: The antonym of CancelAction.
    '''
    class_: Literal['https://schema.org/CancelAction'] = Field( # type: ignore
        default='https://schema.org/CancelAction',
        alias='@type',
        serialization_alias='@type'
    )
