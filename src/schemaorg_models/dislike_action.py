from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .react_action import ReactAction

class DislikeAction(ReactAction):
    """
The act of expressing a negative sentiment about the object. An agent dislikes an object (a proposition, topic or theme) with participants.
    """
    class_: Literal['https://schema.org/DislikeAction'] = Field( # type: ignore
        default='https://schema.org/DislikeAction',
        alias='@type',
        serialization_alias='@type'
    )
