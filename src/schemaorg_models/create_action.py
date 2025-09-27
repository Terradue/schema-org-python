from typing import Literal
from pydantic import Field
from schemaorg_models.action import Action


class CreateAction(Action):
    """
The act of deliberately creating/producing/generating/building a result out of the agent.
    """
    type_: Literal['https://schema.org/CreateAction'] = Field(default='https://schema.org/CreateAction', alias='@type', serialization_alias='@type') # type: ignore
