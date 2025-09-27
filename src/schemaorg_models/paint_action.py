from typing import Literal
from pydantic import Field
from schemaorg_models.create_action import CreateAction


class PaintAction(CreateAction):
    """
The act of producing a painting, typically with paint and canvas as instruments.
    """
    class_: Literal['https://schema.org/PaintAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
