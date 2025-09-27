from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class UserInteraction(Event):
    """
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].
    """
    type_: Literal['https://schema.org/UserInteraction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/UserInteraction'),serialization_alias='class') # type: ignore
