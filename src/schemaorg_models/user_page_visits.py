from typing import Literal
from pydantic import Field
from schemaorg_models.user_interaction import UserInteraction


class UserPageVisits(UserInteraction):
    """
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].
    """
    type_: Literal['https://schema.org/UserPageVisits'] = Field(default='https://schema.org/UserPageVisits', alias='@type', serialization_alias='@type') # type: ignore
