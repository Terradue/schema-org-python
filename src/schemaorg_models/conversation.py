from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Conversation(CreativeWork):
    """
One or more messages between organizations or people on a particular topic. Individual messages can be linked to the conversation with isPartOf or hasPart properties.
    """
    type_: Literal['https://schema.org/Conversation'] = Field(default='https://schema.org/Conversation', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
