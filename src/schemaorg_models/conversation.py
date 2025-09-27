from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Conversation(CreativeWork):
    """
One or more messages between organizations or people on a particular topic. Individual messages can be linked to the conversation with isPartOf or hasPart properties.
    """
    type_: Literal['https://schema.org/Conversation'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Conversation'),serialization_alias='class') # type: ignore
