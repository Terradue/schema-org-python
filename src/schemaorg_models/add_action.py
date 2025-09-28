from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .update_action import UpdateAction

class AddAction(UpdateAction):
    """
The act of editing by adding an object to a collection.
    """
    class_: Literal['https://schema.org/AddAction'] = Field( # type: ignore
        default='https://schema.org/AddAction',
        alias='@type',
        serialization_alias='@type'
    )
