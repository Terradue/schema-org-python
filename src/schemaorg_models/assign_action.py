from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .allocate_action import AllocateAction

class AssignAction(AllocateAction):
    """
The act of allocating an action/event/task to some destination (someone or something).
    """
    class_: Literal['https://schema.org/AssignAction'] = Field( # type: ignore
        default='https://schema.org/AssignAction',
        alias='@type',
        serialization_alias='@type'
    )
