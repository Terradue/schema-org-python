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
from .update_action import UpdateAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .thing import Thing

class ReplaceAction(UpdateAction):
    '''
    The act of editing a recipient by replacing an old object with a new object.

    Attributes:
        replacer: A sub property of object. The object that replaces.
        replacee: A sub property of object. The object that is being replaced.
    '''
    class_: Literal['https://schema.org/ReplaceAction'] = Field( # type: ignore
        default='https://schema.org/ReplaceAction',
        alias='@type',
        serialization_alias='@type'
    )
    replacer: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    replacee: Optional[Union['Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
