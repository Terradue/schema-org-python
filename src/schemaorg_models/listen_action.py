from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class ListenAction(ConsumeAction):
    """
The act of consuming audio content.
    """
    type_: Literal['https://schema.org/ListenAction'] = Field(default='https://schema.org/ListenAction', alias='@type', serialization_alias='@type') # type: ignore
