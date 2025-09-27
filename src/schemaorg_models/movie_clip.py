from typing import Literal
from pydantic import Field
from schemaorg_models.clip import Clip


class MovieClip(Clip):
    """
A short segment/part of a movie.
    """
    type_: Literal['https://schema.org/MovieClip'] = Field(default='https://schema.org/MovieClip', alias='@type', serialization_alias='@type') # type: ignore
