from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.consume_action import ConsumeAction


class EatAction(ConsumeAction):
    """
The act of swallowing solid objects.
    """
    type_: Literal['https://schema.org/EatAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/EatAction'),serialization_alias='class') # type: ignore
