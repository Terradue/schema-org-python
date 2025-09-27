from typing import Literal
from pydantic import Field
from schemaorg_models.react_action import ReactAction


class LikeAction(ReactAction):
    """
The act of expressing a positive sentiment about the object. An agent likes an object (a proposition, topic or theme) with participants.
    """
    class_: Literal['https://schema.org/LikeAction'] = Field(default='https://schema.org/LikeAction', alias='class', serialization_alias='class') # type: ignore
