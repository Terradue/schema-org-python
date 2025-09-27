from typing import Literal
from pydantic import Field
from schemaorg_models.action import Action


class InteractAction(Action):
    """
The act of interacting with another person or organization.
    """
    class_: Literal['https://schema.org/InteractAction'] = Field(default='https://schema.org/InteractAction', alias='class', serialization_alias='class') # type: ignore
