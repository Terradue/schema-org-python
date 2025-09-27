from typing import Literal
from pydantic import Field
from schemaorg_models.control_action import ControlAction


class ResumeAction(ControlAction):
    """
The act of resuming a device or application which was formerly paused (e.g. resume music playback or resume a timer).
    """
    class_: Literal['https://schema.org/ResumeAction'] = Field(default='https://schema.org/ResumeAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
