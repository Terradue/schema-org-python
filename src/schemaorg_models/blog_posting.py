from typing import Literal
from pydantic import Field
from schemaorg_models.social_media_posting import SocialMediaPosting


class BlogPosting(SocialMediaPosting):
    """
A blog post.
    """
    class_: Literal['https://schema.org/BlogPosting'] = Field('class', alias='class', serialization_alias='class') # type: ignore
