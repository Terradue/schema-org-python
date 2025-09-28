from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.user_interaction import UserInteraction

from pydantic import (
    Field
)
from typing import (
    Literal
)

class UserCheckins(UserInteraction):
    """
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].
    """
    class_: Literal['https://schema.org/UserCheckins'] = Field( # type: ignore
        default='https://schema.org/UserCheckins',
        alias='@type',
        serialization_alias='@type'
    )
