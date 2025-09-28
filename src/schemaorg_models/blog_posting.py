from __future__ import annotations

from .social_media_posting import SocialMediaPosting    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BlogPosting(SocialMediaPosting):
    """
A blog post.
    """
    class_: Literal['https://schema.org/BlogPosting'] = Field( # type: ignore
        default='https://schema.org/BlogPosting',
        alias='@type',
        serialization_alias='@type'
    )
