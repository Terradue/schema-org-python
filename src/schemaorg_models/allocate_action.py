from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .organize_action import OrganizeAction

class AllocateAction(OrganizeAction):
    """
The act of organizing tasks/objects/events by associating resources to it.
    """
    class_: Literal['https://schema.org/AllocateAction'] = Field( # type: ignore
        default='https://schema.org/AllocateAction',
        alias='@type',
        serialization_alias='@type'
    )
