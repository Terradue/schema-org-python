from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action


class ControlAction(Action):
    """
An agent controls a device or application.
    """
    type_: Literal['https://schema.org/ControlAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ControlAction'),serialization_alias='class') # type: ignore
