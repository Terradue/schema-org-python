from typing import Literal
from pydantic import Field
from schemaorg_models.react_action import ReactAction


class DisagreeAction(ReactAction):
    """
The act of expressing a difference of opinion with the object. An agent disagrees to/about an object (a proposition, topic or theme) with participants.
    """
    type_: Literal['https://schema.org/DisagreeAction'] = Field(default='https://schema.org/DisagreeAction', alias='@type', serialization_alias='@type') # type: ignore
