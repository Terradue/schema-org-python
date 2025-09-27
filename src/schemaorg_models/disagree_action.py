from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.react_action import ReactAction


class DisagreeAction(ReactAction):
    """
The act of expressing a difference of opinion with the object. An agent disagrees to/about an object (a proposition, topic or theme) with participants.
    """
    type_: Literal['https://schema.org/DisagreeAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DisagreeAction'),serialization_alias='class') # type: ignore
