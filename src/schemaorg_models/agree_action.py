from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .react_action import ReactAction

class AgreeAction(ReactAction):
    """
The act of expressing a consistency of opinion with the object. An agent agrees to/about an object (a proposition, topic or theme) with participants.
    """
    class_: Literal['https://schema.org/AgreeAction'] = Field( # type: ignore
        default='https://schema.org/AgreeAction',
        alias='@type',
        serialization_alias='@type'
    )
