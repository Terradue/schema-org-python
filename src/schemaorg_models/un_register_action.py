from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.interact_action import InteractAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class UnRegisterAction(InteractAction):
    """
The act of un-registering from a service.\
\
Related actions:\
\
* [[RegisterAction]]: antonym of UnRegisterAction.\
* [[LeaveAction]]: Unlike LeaveAction, UnRegisterAction implies that you are unregistering from a service you were previously registered, rather than leaving a team/group of people.
    """
    class_: Literal['https://schema.org/UnRegisterAction'] = Field( # type: ignore
        default='https://schema.org/UnRegisterAction',
        alias='@type',
        serialization_alias='@type'
    )
