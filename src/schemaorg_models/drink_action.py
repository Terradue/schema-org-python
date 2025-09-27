from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.consume_action import ConsumeAction


class DrinkAction(ConsumeAction):
    """
The act of swallowing liquids.
    """
    type_: Literal['https://schema.org/DrinkAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DrinkAction'),serialization_alias='class') # type: ignore
