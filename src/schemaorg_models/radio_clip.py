from typing import Literal
from pydantic import Field
from schemaorg_models.clip import Clip


class RadioClip(Clip):
    """
A short radio program or a segment/part of a radio program.
    """
    class_: Literal['https://schema.org/RadioClip'] = Field('class', alias='class', serialization_alias='class') # type: ignore
