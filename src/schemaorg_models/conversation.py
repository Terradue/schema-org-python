from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.creative_work import CreativeWork

from pydantic import (
    Field
)
from typing import (
    Literal
)

class Conversation(CreativeWork):
    """
One or more messages between organizations or people on a particular topic. Individual messages can be linked to the conversation with isPartOf or hasPart properties.
    """
    class_: Literal['https://schema.org/Conversation'] = Field( # type: ignore
        default='https://schema.org/Conversation',
        alias='@type',
        serialization_alias='@type'
    )
