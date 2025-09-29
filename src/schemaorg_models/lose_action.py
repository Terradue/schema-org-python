from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
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
    '''
    The act of being defeated in a competitive activity.

    Attributes:
        winner: A sub property of participant. The winner of the action.
    '''
    class_: Literal['https://schema.org/LoseAction'] = Field( # type: ignore
        default='https://schema.org/LoseAction',
        alias='@type',
        serialization_alias='@type'
    )
    winner: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
