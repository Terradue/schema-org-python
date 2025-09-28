from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .inform_action import InformAction

class ConfirmAction(InformAction):
    """
The act of notifying someone that a future event/action is going to happen as expected.\
\
Related actions:\
\
* [[CancelAction]]: The antonym of ConfirmAction.
    """
    class_: Literal['https://schema.org/ConfirmAction'] = Field( # type: ignore
        default='https://schema.org/ConfirmAction',
        alias='@type',
        serialization_alias='@type'
    )
