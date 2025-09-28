from __future__ import annotations

from .message import Message    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class EmailMessage(Message):
    """
An email message.
    """
    class_: Literal['https://schema.org/EmailMessage'] = Field( # type: ignore
        default='https://schema.org/EmailMessage',
        alias='@type',
        serialization_alias='@type'
    )
