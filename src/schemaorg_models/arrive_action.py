from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.move_action import MoveAction


class ArriveAction(MoveAction):
    """
The act of arriving at a place. An agent arrives at a destination from a fromLocation, optionally with participants.
    """
    type_: Literal['https://schema.org/ArriveAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ArriveAction'),serialization_alias='class') # type: ignore
