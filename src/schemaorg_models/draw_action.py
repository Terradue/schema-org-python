from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.create_action import CreateAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DrawAction(CreateAction):
    """
The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments.
    """
    class_: Literal['https://schema.org/DrawAction'] = Field( # type: ignore
        default='https://schema.org/DrawAction',
        alias='@type',
        serialization_alias='@type'
    )
