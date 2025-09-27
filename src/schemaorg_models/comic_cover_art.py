from typing import Literal
from pydantic import Field
from schemaorg_models.comic_story import ComicStory


class ComicCoverArt(ComicStory):
    """
The artwork on the cover of a comic.
    """
    class_: Literal['https://schema.org/ComicCoverArt'] = Field('class', alias='class', serialization_alias='class') # type: ignore
