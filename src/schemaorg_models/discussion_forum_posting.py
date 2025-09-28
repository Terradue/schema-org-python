from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.social_media_posting import SocialMediaPosting

from pydantic import (
    Field
)
from typing import (
    Literal
)

class DiscussionForumPosting(SocialMediaPosting):
    """
A posting to a discussion forum.
    """
    class_: Literal['https://schema.org/DiscussionForumPosting'] = Field( # type: ignore
        default='https://schema.org/DiscussionForumPosting',
        alias='@type',
        serialization_alias='@type'
    )
