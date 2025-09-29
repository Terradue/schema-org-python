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
from .organize_action import OrganizeAction

class BookmarkAction(OrganizeAction):
    '''
    An agent bookmarks/flags/labels/tags/marks an object.
    '''
    class_: Literal['https://schema.org/BookmarkAction'] = Field( # type: ignore
        default='https://schema.org/BookmarkAction',
        alias='@type',
        serialization_alias='@type'
    )
