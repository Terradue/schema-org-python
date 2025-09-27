from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class DrinkAction(ConsumeAction):
    """
The act of swallowing liquids.
    """
    class_: Literal['https://schema.org/DrinkAction'] = Field(default='https://schema.org/DrinkAction', alias='class', serialization_alias='class') # type: ignore
