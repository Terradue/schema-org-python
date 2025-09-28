from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.article import Article

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AdvertiserContentArticle(Article):
    """
An [[Article]] that an external entity has paid to place or to produce to its specifications. Includes [advertorials](https://en.wikipedia.org/wiki/Advertorial), sponsored content, native advertising and other paid content.
    """
    class_: Literal['https://schema.org/AdvertiserContentArticle'] = Field( # type: ignore
        default='https://schema.org/AdvertiserContentArticle',
        alias='@type',
        serialization_alias='@type'
    )
