from typing import Literal
from pydantic import Field
from schemaorg_models.communicate_action import CommunicateAction


class CheckInAction(CommunicateAction):
    """
The act of an agent communicating (service provider, social media, etc) their arrival by registering/confirming for a previously reserved service (e.g. flight check-in) or at a place (e.g. hotel), possibly resulting in a result (boarding pass, etc).\
\
Related actions:\
\
* [[CheckOutAction]]: The antonym of CheckInAction.\
* [[ArriveAction]]: Unlike ArriveAction, CheckInAction implies that the agent is informing/confirming the start of a previously reserved service.\
* [[ConfirmAction]]: Unlike ConfirmAction, CheckInAction implies that the agent is informing/confirming the *start* of a previously reserved service rather than its validity/existence.
    """
    class_: Literal['https://schema.org/CheckInAction'] = Field(default='https://schema.org/CheckInAction', alias='class', serialization_alias='class') # type: ignore
