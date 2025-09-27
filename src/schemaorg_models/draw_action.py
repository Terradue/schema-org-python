from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.create_action import CreateAction


class DrawAction(CreateAction):
    """
The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments.
    """
    type_: Literal['https://schema.org/DrawAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DrawAction'),serialization_alias='class') # type: ignore
