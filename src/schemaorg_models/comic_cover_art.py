from typing import Literal
from pydantic import Field
from schemaorg_models.comic_story import ComicStory


class ComicCoverArt(ComicStory):
    """
The artwork on the cover of a comic.
    """
    type_: Literal['https://schema.org/ComicCoverArt'] = Field(default='https://schema.org/ComicCoverArt', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
