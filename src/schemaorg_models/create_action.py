from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .action import Action

class CreateAction(Action):
    """
The act of deliberately creating/producing/generating/building a result out of the agent.
    """
    class_: Literal['https://schema.org/CreateAction'] = Field( # type: ignore
        default='https://schema.org/CreateAction',
        alias='@type',
        serialization_alias='@type'
    )
