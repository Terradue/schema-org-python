from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .person import Person
from .achieve_action import AchieveAction

class WinAction(AchieveAction):
    """
The act of achieving victory in a competitive activity.
    """
    class_: Literal['https://schema.org/WinAction'] = Field( # type: ignore
        default='https://schema.org/WinAction',
        alias='@type',
        serialization_alias='@type'
    )
    loser: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'loser',
            'https://schema.org/loser'
        ),
        serialization_alias='https://schema.org/loser'
    )
