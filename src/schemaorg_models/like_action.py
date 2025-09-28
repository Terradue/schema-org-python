from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .react_action import ReactAction

class LikeAction(ReactAction):
    """
The act of expressing a positive sentiment about the object. An agent likes an object (a proposition, topic or theme) with participants.
    """
    class_: Literal['https://schema.org/LikeAction'] = Field( # type: ignore
        default='https://schema.org/LikeAction',
        alias='@type',
        serialization_alias='@type'
    )
