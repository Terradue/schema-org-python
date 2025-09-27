from typing import Literal
from pydantic import Field
from schemaorg_models.react_action import ReactAction


class AgreeAction(ReactAction):
    """
The act of expressing a consistency of opinion with the object. An agent agrees to/about an object (a proposition, topic or theme) with participants.
    """
    class_: Literal['https://schema.org/AgreeAction'] = Field(default='https://schema.org/AgreeAction', alias='class', serialization_alias='class') # type: ignore
