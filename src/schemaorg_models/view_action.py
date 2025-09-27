from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.consume_action import ConsumeAction


class ViewAction(ConsumeAction):
    """
The act of consuming static visual content.
    """
    type_: Literal['https://schema.org/ViewAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ViewAction'),serialization_alias='class') # type: ignore
