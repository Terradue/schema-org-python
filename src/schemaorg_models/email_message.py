from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.message import Message


class EmailMessage(Message):
    """
An email message.
    """
    type_: Literal['https://schema.org/EmailMessage'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/EmailMessage'),serialization_alias='class') # type: ignore
