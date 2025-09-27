from typing import Literal
from pydantic import Field
from schemaorg_models.control_action import ControlAction


class SuspendAction(ControlAction):
    """
The act of momentarily pausing a device or application (e.g. pause music playback or pause a timer).
    """
    type_: Literal['https://schema.org/SuspendAction'] = Field(default='https://schema.org/SuspendAction', alias='@type', serialization_alias='@type') # type: ignore
