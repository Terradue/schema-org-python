from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Conversation(CreativeWork):
    """
One or more messages between organizations or people on a particular topic. Individual messages can be linked to the conversation with isPartOf or hasPart properties.
    """
    class_: Literal['https://schema.org/Conversation'] = Field(default='https://schema.org/Conversation', alias='class', serialization_alias='class') # type: ignore
