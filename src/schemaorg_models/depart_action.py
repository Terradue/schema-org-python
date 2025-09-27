from typing import Literal
from pydantic import Field
from schemaorg_models.move_action import MoveAction


class DepartAction(MoveAction):
    """
The act of  departing from a place. An agent departs from a fromLocation for a destination, optionally with participants.
    """
    class_: Literal['https://schema.org/DepartAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
