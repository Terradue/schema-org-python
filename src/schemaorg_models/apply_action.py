from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .organize_action import OrganizeAction

class ApplyAction(OrganizeAction):
    """
The act of registering to an organization/service without the guarantee to receive it.\
\
Related actions:\
\
* [[RegisterAction]]: Unlike RegisterAction, ApplyAction has no guarantees that the application will be accepted.
    """
    class_: Literal['https://schema.org/ApplyAction'] = Field( # type: ignore
        default='https://schema.org/ApplyAction',
        alias='@type',
        serialization_alias='@type'
    )
