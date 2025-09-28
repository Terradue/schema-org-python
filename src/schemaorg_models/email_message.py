from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .message import Message

class EmailMessage(Message):
    """
An email message.
    """
    class_: Literal['https://schema.org/EmailMessage'] = Field( # type: ignore
        default='https://schema.org/EmailMessage',
        alias='@type',
        serialization_alias='@type'
    )
