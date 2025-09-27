from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.create_action import CreateAction


class PaintAction(CreateAction):
    """
The act of producing a painting, typically with paint and canvas as instruments.
    """
    type_: Literal['https://schema.org/PaintAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PaintAction'),serialization_alias='class') # type: ignore
