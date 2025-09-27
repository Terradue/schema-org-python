from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.control_action import ControlAction


class SuspendAction(ControlAction):
    """
The act of momentarily pausing a device or application (e.g. pause music playback or pause a timer).
    """
    type_: Literal['https://schema.org/SuspendAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/SuspendAction'),serialization_alias='class') # type: ignore
