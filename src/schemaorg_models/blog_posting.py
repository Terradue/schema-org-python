from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.social_media_posting import SocialMediaPosting


class BlogPosting(SocialMediaPosting):
    """
A blog post.
    """
    type_: Literal['https://schema.org/BlogPosting'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BlogPosting'),serialization_alias='class') # type: ignore
