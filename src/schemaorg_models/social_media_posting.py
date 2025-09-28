from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.article import Article

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.creative_work import CreativeWork

class SocialMediaPosting(Article):
    """
A post to a social media platform, including blog posts, tweets, Facebook posts, etc.
    """
    class_: Literal['https://schema.org/SocialMediaPosting'] = Field( # type: ignore
        default='https://schema.org/SocialMediaPosting',
        alias='@type',
        serialization_alias='@type'
    )
    sharedContent: Optional[Union[CreativeWork, List[CreativeWork]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sharedContent',
            'https://schema.org/sharedContent'
        ),
        serialization_alias='https://schema.org/sharedContent'
    )
