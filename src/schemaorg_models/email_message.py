from typing import Literal
from pydantic import Field
from schemaorg_models.message import Message


class EmailMessage(Message):
    """
An email message.
    """
    class_: Literal['https://schema.org/EmailMessage'] = Field(default='https://schema.org/EmailMessage', alias='class', serialization_alias='class') # type: ignore
