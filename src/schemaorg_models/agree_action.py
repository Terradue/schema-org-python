from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.react_action import ReactAction


class AgreeAction(ReactAction):
    """
The act of expressing a consistency of opinion with the object. An agent agrees to/about an object (a proposition, topic or theme) with participants.
    """
    type_: Literal['https://schema.org/AgreeAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AgreeAction'),serialization_alias='class') # type: ignore
