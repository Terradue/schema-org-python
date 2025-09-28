from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.message import Message

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
