from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action


class InteractAction(Action):
    """
The act of interacting with another person or organization.
    """
    type_: Literal['https://schema.org/InteractAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/InteractAction'),serialization_alias='class') # type: ignore
