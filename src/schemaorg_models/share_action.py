from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.communicate_action import CommunicateAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ShareAction(CommunicateAction):
    """
The act of distributing content to people for their amusement or edification.
    """
    class_: Literal['https://schema.org/ShareAction'] = Field( # type: ignore
        default='https://schema.org/ShareAction',
        alias='@type',
        serialization_alias='@type'
    )
