from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.control_action import ControlAction


class DeactivateAction(ControlAction):
    """
The act of stopping or deactivating a device or application (e.g. stopping a timer or turning off a flashlight).
    """
    type_: Literal['https://schema.org/DeactivateAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DeactivateAction'),serialization_alias='class') # type: ignore
