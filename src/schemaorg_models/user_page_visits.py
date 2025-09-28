from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .user_interaction import UserInteraction

class UserPageVisits(UserInteraction):
    """
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].
    """
    class_: Literal['https://schema.org/UserPageVisits'] = Field( # type: ignore
        default='https://schema.org/UserPageVisits',
        alias='@type',
        serialization_alias='@type'
    )
