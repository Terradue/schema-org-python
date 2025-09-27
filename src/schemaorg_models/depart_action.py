from typing import Literal
from pydantic import Field
from schemaorg_models.move_action import MoveAction


class DepartAction(MoveAction):
    """
The act of  departing from a place. An agent departs from a fromLocation for a destination, optionally with participants.
    """
    type_: Literal['https://schema.org/DepartAction'] = Field(default='https://schema.org/DepartAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
