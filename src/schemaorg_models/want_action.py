from typing import Literal
from pydantic import Field
from schemaorg_models.react_action import ReactAction


class WantAction(ReactAction):
    """
The act of expressing a desire about the object. An agent wants an object.
    """
    class_: Literal['https://schema.org/WantAction'] = Field(default='https://schema.org/WantAction', alias='@type', serialization_alias='@type') # type: ignore
