from typing import Literal
from pydantic import Field
from schemaorg_models.clip import Clip


class MovieClip(Clip):
    """
A short segment/part of a movie.
    """
    class_: Literal['https://schema.org/MovieClip'] = Field('class', alias='class', serialization_alias='class') # type: ignore
