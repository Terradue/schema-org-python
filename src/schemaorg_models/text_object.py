from typing import Literal
from pydantic import Field
from schemaorg_models.media_object import MediaObject


class TextObject(MediaObject):
    """
A text file. The text can be unformatted or contain markup, html, etc.
    """
    class_: Literal['https://schema.org/TextObject'] = Field(default='https://schema.org/TextObject', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
