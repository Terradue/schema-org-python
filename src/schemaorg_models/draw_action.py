from typing import Literal
from pydantic import Field
from schemaorg_models.create_action import CreateAction


class DrawAction(CreateAction):
    """
The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments.
    """
    class_: Literal['https://schema.org/DrawAction'] = Field(default='https://schema.org/DrawAction', alias='class', serialization_alias='class') # type: ignore
