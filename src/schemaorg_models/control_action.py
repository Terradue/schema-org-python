from typing import Literal
from pydantic import Field
from schemaorg_models.action import Action


class ControlAction(Action):
    """
An agent controls a device or application.
    """
    type_: Literal['https://schema.org/ControlAction'] = Field(default='https://schema.org/ControlAction', alias='@type', serialization_alias='@type') # type: ignore
