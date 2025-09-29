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
from .action import Action
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .place import Place

class MoveAction(Action):
    '''
    The act of an agent relocating to a place.\
\
Related actions:\
\
* [[TransferAction]]: Unlike TransferAction, the subject of the move is a living Person or Organization rather than an inanimate object.

    Attributes:
        toLocation: A sub property of location. The final location of the object or the agent after the action.
        fromLocation: A sub property of location. The original location of the object or the agent before the action.
    '''
    class_: Literal['https://schema.org/MoveAction'] = Field( # type: ignore
        default='https://schema.org/MoveAction',
        alias='@type',
        serialization_alias='@type'
    )
    toLocation: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'toLocation',
            'https://schema.org/toLocation'
        ),
        serialization_alias='https://schema.org/toLocation'
    )
    fromLocation: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fromLocation',
            'https://schema.org/fromLocation'
        ),
        serialization_alias='https://schema.org/fromLocation'
    )
