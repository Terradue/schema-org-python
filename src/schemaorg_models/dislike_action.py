from typing import Literal
from pydantic import Field
from schemaorg_models.react_action import ReactAction


class DislikeAction(ReactAction):
    """
The act of expressing a negative sentiment about the object. An agent dislikes an object (a proposition, topic or theme) with participants.
    """
    type_: Literal['https://schema.org/DislikeAction'] = Field(default='https://schema.org/DislikeAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
