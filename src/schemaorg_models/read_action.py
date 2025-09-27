from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.consume_action import ConsumeAction


class ReadAction(ConsumeAction):
    """
The act of consuming written content.
    """
    type_: Literal['https://schema.org/ReadAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ReadAction'),serialization_alias='class') # type: ignore
