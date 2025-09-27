from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class UseAction(ConsumeAction):
    """
The act of applying an object to its intended purpose.
    """
    type_: Literal['https://schema.org/UseAction'] = Field(default='https://schema.org/UseAction', alias='@type', serialization_alias='@type') # type: ignore
