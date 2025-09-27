from typing import Literal
from pydantic import Field
from schemaorg_models.message import Message


class EmailMessage(Message):
    """
An email message.
    """
    type_: Literal['https://schema.org/EmailMessage'] = Field(default='https://schema.org/EmailMessage', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
