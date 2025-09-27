from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.consume_action import ConsumeAction


class ListenAction(ConsumeAction):
    """
The act of consuming audio content.
    """
    type_: Literal['https://schema.org/ListenAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ListenAction'),serialization_alias='class') # type: ignore
