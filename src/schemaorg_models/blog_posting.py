from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .social_media_posting import SocialMediaPosting

class BlogPosting(SocialMediaPosting):
    """
A blog post.
    """
    class_: Literal['https://schema.org/BlogPosting'] = Field( # type: ignore
        default='https://schema.org/BlogPosting',
        alias='@type',
        serialization_alias='@type'
    )
