from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class ListenAction(ConsumeAction):
    """
The act of consuming audio content.
    """
    class_: Literal['https://schema.org/ListenAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
