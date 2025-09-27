from typing import Literal
from pydantic import Field
from schemaorg_models.move_action import MoveAction


class ArriveAction(MoveAction):
    """
The act of arriving at a place. An agent arrives at a destination from a fromLocation, optionally with participants.
    """
    class_: Literal['https://schema.org/ArriveAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
