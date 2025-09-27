from typing import Literal
from pydantic import Field
from schemaorg_models.create_action import CreateAction


class DrawAction(CreateAction):
    """
The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments.
    """
    class_: Literal['https://schema.org/DrawAction'] = Field(default='https://schema.org/DrawAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
