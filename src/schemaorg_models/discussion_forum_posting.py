from __future__ import annotations

from .social_media_posting import SocialMediaPosting    

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
