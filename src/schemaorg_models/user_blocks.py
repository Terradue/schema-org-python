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
from .user_interaction import UserInteraction

class UserBlocks(UserInteraction):
    '''
    UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].
    '''
    class_: Literal['https://schema.org/UserBlocks'] = Field( # type: ignore
        default='https://schema.org/UserBlocks',
        alias='@type',
        serialization_alias='@type'
    )
