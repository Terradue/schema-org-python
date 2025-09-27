from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.media_object import MediaObject


class TextObject(MediaObject):
    """
A text file. The text can be unformatted or contain markup, html, etc.
    """
    type_: Literal['https://schema.org/TextObject'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TextObject'),serialization_alias='class') # type: ignore
