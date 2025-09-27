from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.react_action import ReactAction


class WantAction(ReactAction):
    """
The act of expressing a desire about the object. An agent wants an object.
    """
    type_: Literal['https://schema.org/WantAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/WantAction'),serialization_alias='class') # type: ignore
