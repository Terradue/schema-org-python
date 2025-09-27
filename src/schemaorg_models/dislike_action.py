from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.react_action import ReactAction


class DislikeAction(ReactAction):
    """
The act of expressing a negative sentiment about the object. An agent dislikes an object (a proposition, topic or theme) with participants.
    """
    type_: Literal['https://schema.org/DislikeAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DislikeAction'),serialization_alias='class') # type: ignore
