from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.action import Action

from pydantic import (
    Field
)
from typing import (
    Literal
)

class ControlAction(Action):
    """
An agent controls a device or application.
    """
    class_: Literal['https://schema.org/ControlAction'] = Field( # type: ignore
        default='https://schema.org/ControlAction',
        alias='@type',
        serialization_alias='@type'
    )
