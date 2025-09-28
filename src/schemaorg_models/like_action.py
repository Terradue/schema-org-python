from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.react_action import ReactAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class LikeAction(ReactAction):
    """
The act of expressing a positive sentiment about the object. An agent likes an object (a proposition, topic or theme) with participants.
    """
    class_: Literal['https://schema.org/LikeAction'] = Field( # type: ignore
        default='https://schema.org/LikeAction',
        alias='@type',
        serialization_alias='@type'
    )
