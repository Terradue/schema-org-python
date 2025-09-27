from typing import Literal
from pydantic import Field
from schemaorg_models.action import Action


class InteractAction(Action):
    """
The act of interacting with another person or organization.
    """
    type_: Literal['https://schema.org/InteractAction'] = Field(default='https://schema.org/InteractAction', alias='@type', serialization_alias='@type') # type: ignore
