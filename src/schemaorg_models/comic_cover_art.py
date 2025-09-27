from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.comic_story import ComicStory


class ComicCoverArt(ComicStory):
    """
The artwork on the cover of a comic.
    """
    type_: Literal['https://schema.org/ComicCoverArt'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ComicCoverArt'),serialization_alias='class') # type: ignore
