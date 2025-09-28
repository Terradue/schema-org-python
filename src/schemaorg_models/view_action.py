from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .consume_action import ConsumeAction

class ViewAction(ConsumeAction):
    """
The act of consuming static visual content.
    """
    class_: Literal['https://schema.org/ViewAction'] = Field( # type: ignore
        default='https://schema.org/ViewAction',
        alias='@type',
        serialization_alias='@type'
    )
