from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.react_action import ReactAction


class LikeAction(ReactAction):
    """
The act of expressing a positive sentiment about the object. An agent likes an object (a proposition, topic or theme) with participants.
    """
    type_: Literal['https://schema.org/LikeAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/LikeAction'),serialization_alias='class') # type: ignore
