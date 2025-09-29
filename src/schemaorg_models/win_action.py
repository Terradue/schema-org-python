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

class WinAction(AchieveAction):
    '''
    The act of achieving victory in a competitive activity.

    Attributes:
        loser: A sub property of participant. The loser of the action.
    '''
    class_: Literal['https://schema.org/WinAction'] = Field( # type: ignore
        default='https://schema.org/WinAction',
        alias='@type',
        serialization_alias='@type'
    )
    loser: Optional[Union['Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
