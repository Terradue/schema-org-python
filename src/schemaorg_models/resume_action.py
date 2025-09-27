from typing import Literal
from pydantic import Field
from schemaorg_models.control_action import ControlAction


class ResumeAction(ControlAction):
    """
The act of resuming a device or application which was formerly paused (e.g. resume music playback or resume a timer).
    """
    class_: Literal['https://schema.org/ResumeAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
