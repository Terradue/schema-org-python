from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.control_action import ControlAction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class SuspendAction(ControlAction):
    """
The act of momentarily pausing a device or application (e.g. pause music playback or pause a timer).
    """
    class_: Literal['https://schema.org/SuspendAction'] = Field( # type: ignore
        default='https://schema.org/SuspendAction',
        alias='@type',
        serialization_alias='@type'
    )
