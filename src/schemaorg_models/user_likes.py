from __future__ import annotations

from .user_interaction import UserInteraction    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class UserLikes(UserInteraction):
    """
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].
    """
    class_: Literal['https://schema.org/UserLikes'] = Field( # type: ignore
        default='https://schema.org/UserLikes',
        alias='@type',
        serialization_alias='@type'
    )
