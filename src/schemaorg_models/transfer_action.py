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

class TransferAction(Action):
    '''
    The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.

    Attributes:
        fromLocation: A sub property of location. The original location of the object or the agent before the action.
        toLocation: A sub property of location. The final location of the object or the agent after the action.
    '''
    class_: Literal['https://schema.org/TransferAction'] = Field( # type: ignore
        default='https://schema.org/TransferAction',
        alias='@type',
        serialization_alias='@type'
    )
    fromLocation: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fromLocation',
            'https://schema.org/fromLocation'
        ),
        serialization_alias='https://schema.org/fromLocation'
    )
    toLocation: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'toLocation',
            'https://schema.org/toLocation'
        ),
        serialization_alias='https://schema.org/toLocation'
    )
