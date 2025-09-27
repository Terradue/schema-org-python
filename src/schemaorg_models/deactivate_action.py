from typing import Literal
from pydantic import Field
from schemaorg_models.control_action import ControlAction


class DeactivateAction(ControlAction):
    """
The act of stopping or deactivating a device or application (e.g. stopping a timer or turning off a flashlight).
    """
    type_: Literal['https://schema.org/DeactivateAction'] = Field(default='https://schema.org/DeactivateAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
