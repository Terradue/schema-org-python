from typing import Literal
from pydantic import Field
from schemaorg_models.create_action import CreateAction


class PaintAction(CreateAction):
    """
The act of producing a painting, typically with paint and canvas as instruments.
    """
    type_: Literal['https://schema.org/PaintAction'] = Field(default='https://schema.org/PaintAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
