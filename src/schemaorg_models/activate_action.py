from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.control_action import ControlAction


class ActivateAction(ControlAction):
    """
The act of starting or activating a device or application (e.g. starting a timer or turning on a flashlight).
    """
    type_: Literal['https://schema.org/ActivateAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ActivateAction'),serialization_alias='class') # type: ignore
