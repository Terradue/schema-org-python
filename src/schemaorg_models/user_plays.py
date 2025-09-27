from typing import Literal
from pydantic import Field
from schemaorg_models.user_interaction import UserInteraction


class UserPlays(UserInteraction):
    """
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].
    """
    class_: Literal['https://schema.org/UserPlays'] = Field(default='https://schema.org/UserPlays', alias='class', serialization_alias='class') # type: ignore
