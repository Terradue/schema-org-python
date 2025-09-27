from typing import Literal
from pydantic import Field
from schemaorg_models.achieve_action import AchieveAction


class TieAction(AchieveAction):
    """
The act of reaching a draw in a competitive activity.
    """
    class_: Literal['https://schema.org/TieAction'] = Field(default='https://schema.org/TieAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
