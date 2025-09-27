from typing import Literal
from pydantic import Field
from schemaorg_models.action import Action


class ControlAction(Action):
    """
An agent controls a device or application.
    """
    class_: Literal['https://schema.org/ControlAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
