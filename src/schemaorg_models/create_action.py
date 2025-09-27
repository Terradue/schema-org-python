from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action


class CreateAction(Action):
    """
The act of deliberately creating/producing/generating/building a result out of the agent.
    """
    type_: Literal['https://schema.org/CreateAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CreateAction'),serialization_alias='class') # type: ignore
