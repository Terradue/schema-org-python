from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.communicate_action import CommunicateAction


class CheckOutAction(CommunicateAction):
    """
The act of an agent communicating (service provider, social media, etc) their departure of a previously reserved service (e.g. flight check-in) or place (e.g. hotel).\
\
Related actions:\
\
* [[CheckInAction]]: The antonym of CheckOutAction.\
* [[DepartAction]]: Unlike DepartAction, CheckOutAction implies that the agent is informing/confirming the end of a previously reserved service.\
* [[CancelAction]]: Unlike CancelAction, CheckOutAction implies that the agent is informing/confirming the end of a previously reserved service.
    """
    type_: Literal['https://schema.org/CheckOutAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CheckOutAction'),serialization_alias='class') # type: ignore
