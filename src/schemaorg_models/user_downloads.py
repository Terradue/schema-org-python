from typing import Literal
from pydantic import Field
from schemaorg_models.user_interaction import UserInteraction


class UserDownloads(UserInteraction):
    """
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].
    """
    class_: Literal['https://schema.org/UserDownloads'] = Field(default='https://schema.org/UserDownloads', alias='@type', serialization_alias='@type') # type: ignore
