from typing import Literal
from pydantic import Field
from schemaorg_models.move_action import MoveAction


class ArriveAction(MoveAction):
    """
The act of arriving at a place. An agent arrives at a destination from a fromLocation, optionally with participants.
    """
    class_: Literal['https://schema.org/ArriveAction'] = Field(default='https://schema.org/ArriveAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
