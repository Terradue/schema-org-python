from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.clip import Clip


class RadioClip(Clip):
    """
A short radio program or a segment/part of a radio program.
    """
    type_: Literal['https://schema.org/RadioClip'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RadioClip'),serialization_alias='class') # type: ignore
