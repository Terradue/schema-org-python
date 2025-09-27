from typing import Literal
from pydantic import Field
from schemaorg_models.clip import Clip


class RadioClip(Clip):
    """
A short radio program or a segment/part of a radio program.
    """
    type_: Literal['https://schema.org/RadioClip'] = Field(default='https://schema.org/RadioClip', alias='@type', serialization_alias='@type') # type: ignore
