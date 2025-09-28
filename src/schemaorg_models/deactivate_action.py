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

class DeactivateAction(ControlAction):
    """
The act of stopping or deactivating a device or application (e.g. stopping a timer or turning off a flashlight).
    """
    class_: Literal['https://schema.org/DeactivateAction'] = Field( # type: ignore
        default='https://schema.org/DeactivateAction',
        alias='@type',
        serialization_alias='@type'
    )
