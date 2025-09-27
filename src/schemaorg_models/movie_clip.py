from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.clip import Clip


class MovieClip(Clip):
    """
A short segment/part of a movie.
    """
    type_: Literal['https://schema.org/MovieClip'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MovieClip'),serialization_alias='class') # type: ignore
