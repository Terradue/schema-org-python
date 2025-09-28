from __future__ import annotations

from .interact_action import InteractAction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BefriendAction(InteractAction):
    """
The act of forming a personal connection with someone (object) mutually/bidirectionally/symmetrically.\
\
Related actions:\
\
* [[FollowAction]]: Unlike FollowAction, BefriendAction implies that the connection is reciprocal.
    """
    class_: Literal['https://schema.org/BefriendAction'] = Field( # type: ignore
        default='https://schema.org/BefriendAction',
        alias='@type',
        serialization_alias='@type'
    )
