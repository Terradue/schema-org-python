from typing import Literal
from pydantic import Field
from schemaorg_models.action import Action


class ControlAction(Action):
    """
An agent controls a device or application.
    """
    class_: Literal['https://schema.org/ControlAction'] = Field(default='https://schema.org/ControlAction', alias='class', serialization_alias='class') # type: ignore
