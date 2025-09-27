from typing import Literal
from pydantic import Field
from schemaorg_models.control_action import ControlAction


class SuspendAction(ControlAction):
    """
The act of momentarily pausing a device or application (e.g. pause music playback or pause a timer).
    """
    class_: Literal['https://schema.org/SuspendAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
