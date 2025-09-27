from typing import Literal
from pydantic import Field
from schemaorg_models.control_action import ControlAction


class ActivateAction(ControlAction):
    """
The act of starting or activating a device or application (e.g. starting a timer or turning on a flashlight).
    """
    class_: Literal['https://schema.org/ActivateAction'] = Field(default='https://schema.org/ActivateAction', alias='@type', serialization_alias='@type') # type: ignore
