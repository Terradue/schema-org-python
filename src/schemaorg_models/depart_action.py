from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.move_action import MoveAction


class DepartAction(MoveAction):
    """
The act of  departing from a place. An agent departs from a fromLocation for a destination, optionally with participants.
    """
    type_: Literal['https://schema.org/DepartAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DepartAction'),serialization_alias='class') # type: ignore
