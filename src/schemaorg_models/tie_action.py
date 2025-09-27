from typing import Literal
from pydantic import Field
from schemaorg_models.achieve_action import AchieveAction


class TieAction(AchieveAction):
    """
The act of reaching a draw in a competitive activity.
    """
    type_: Literal['https://schema.org/TieAction'] = Field(default='https://schema.org/TieAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
