from typing import Literal
from pydantic import Field
from schemaorg_models.react_action import ReactAction


class LikeAction(ReactAction):
    """
The act of expressing a positive sentiment about the object. An agent likes an object (a proposition, topic or theme) with participants.
    """
    type_: Literal['https://schema.org/LikeAction'] = Field(default='https://schema.org/LikeAction', alias='@type', serialization_alias='@type') # type: ignore
