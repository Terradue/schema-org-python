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
from .achieve_action import AchieveAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .person import Person

class LoseAction(AchieveAction):
    """
The act of being defeated in a competitive activity.
    """
    class_: Literal['https://schema.org/LoseAction'] = Field( # type: ignore
        default='https://schema.org/LoseAction',
        alias='@type',
        serialization_alias='@type'
    )
    winner: Optional[Union[Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'winner',
            'https://schema.org/winner'
        ),
        serialization_alias='https://schema.org/winner'
    )
