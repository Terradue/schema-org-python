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

class ActivateAction(ControlAction):
    """
The act of starting or activating a device or application (e.g. starting a timer or turning on a flashlight).
    """
    class_: Literal['https://schema.org/ActivateAction'] = Field( # type: ignore
        default='https://schema.org/ActivateAction',
        alias='@type',
        serialization_alias='@type'
    )
