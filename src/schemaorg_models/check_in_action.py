from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.communicate_action import CommunicateAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

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
    class_: Literal['https://schema.org/CheckInAction'] = Field( # type: ignore
        default='https://schema.org/CheckInAction',
        alias='@type',
        serialization_alias='@type'
    )
