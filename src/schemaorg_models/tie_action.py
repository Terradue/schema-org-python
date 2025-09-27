from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.achieve_action import AchieveAction


class TieAction(AchieveAction):
    """
The act of reaching a draw in a competitive activity.
    """
    type_: Literal['https://schema.org/TieAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TieAction'),serialization_alias='class') # type: ignore
