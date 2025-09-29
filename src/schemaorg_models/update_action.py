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
    from .thing import Thing

class UpdateAction(Action):
    '''
    The act of managing by changing/editing the state of the object.

    Attributes:
        targetCollection: A sub property of object. The collection target of the action.
        collection: A sub property of object. The collection target of the action.
    '''
    class_: Literal['https://schema.org/UpdateAction'] = Field( # type: ignore
        default='https://schema.org/UpdateAction',
        alias='@type',
        serialization_alias='@type'
    )
    targetCollection: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'targetCollection',
            'https://schema.org/targetCollection'
        ),
        serialization_alias='https://schema.org/targetCollection'
    )
    collection: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'collection',
            'https://schema.org/collection'
        ),
        serialization_alias='https://schema.org/collection'
    )
