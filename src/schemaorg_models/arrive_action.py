from typing import Literal
from pydantic import Field
from schemaorg_models.move_action import MoveAction


class ArriveAction(MoveAction):
    """
The act of arriving at a place. An agent arrives at a destination from a fromLocation, optionally with participants.
    """
    type_: Literal['https://schema.org/ArriveAction'] = Field(default='https://schema.org/ArriveAction', alias='@type', serialization_alias='@type') # type: ignore
