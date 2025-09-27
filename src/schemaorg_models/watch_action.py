from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.consume_action import ConsumeAction


class WatchAction(ConsumeAction):
    """
The act of consuming dynamic/moving visual content.
    """
    type_: Literal['https://schema.org/WatchAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/WatchAction'),serialization_alias='class') # type: ignore
