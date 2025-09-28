from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .communicate_action import CommunicateAction

class ShareAction(CommunicateAction):
    """
The act of distributing content to people for their amusement or edification.
    """
    class_: Literal['https://schema.org/ShareAction'] = Field( # type: ignore
        default='https://schema.org/ShareAction',
        alias='@type',
        serialization_alias='@type'
    )
