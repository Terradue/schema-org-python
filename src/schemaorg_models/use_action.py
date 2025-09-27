from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.consume_action import ConsumeAction


class UseAction(ConsumeAction):
    """
The act of applying an object to its intended purpose.
    """
    type_: Literal['https://schema.org/UseAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/UseAction'),serialization_alias='class') # type: ignore
