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
from .communicate_action import CommunicateAction

class CheckOutAction(CommunicateAction):
    '''
    The act of an agent communicating (service provider, social media, etc) their departure of a previously reserved service (e.g. flight check-in) or place (e.g. hotel).\
\
Related actions:\
\
* [[CheckInAction]]: The antonym of CheckOutAction.\
* [[DepartAction]]: Unlike DepartAction, CheckOutAction implies that the agent is informing/confirming the end of a previously reserved service.\
* [[CancelAction]]: Unlike CancelAction, CheckOutAction implies that the agent is informing/confirming the end of a previously reserved service.
    '''
    class_: Literal['https://schema.org/CheckOutAction'] = Field( # type: ignore
        default='https://schema.org/CheckOutAction',
        alias='@type',
        serialization_alias='@type'
    )
